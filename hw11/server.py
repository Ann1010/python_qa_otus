import re
import socket
from http import HTTPStatus


def handler_client(connection, address):
    client_data = ''
    with connection:
        while True:
            data = connection.recv(1024)
            print('Data:', data)
            if not data:
                break
            client_data += data.decode()
            if '\r\n\r\n' in client_data:
                break
        if client_data:
            client_data = client_data.strip().split('\r\n')
            data = [item for item in client_data[0].split()]
            request_status = re.search(r'status=(\d+)', data[1])
            response_status = f'{HTTPStatus.OK} {HTTPStatus.OK.phrase}'
            if request_status:
                if len(request_status.group(1)) == 3:
                    for status in list(HTTPStatus):
                        if int(request_status.group(1)) == status.value:
                            response_status = f'{status.value} {status.phrase}'

            connection.send(
                (f"HTTP/1.1 {response_status}\r\n"
                 f'\r\nRequest Method: {data[0]}'
                 f'\r\nRequest Source: {address}'
                 f'\r\nResponse Status: {response_status}\r\n'
                 f'{client_data}').encode()
            )


with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 8090))
    s.listen()
    while True:
        client_conn, client_address = s.accept()
        handler_client(client_conn, client_address)
        print(f"Sent data to {client_address}")
