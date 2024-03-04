import json
import os
import re


def top_duration(res):
    """ Топ-3 запросов по длительности"""
    data = []
    for row in res:
        temp = {}
        ip = re.search(r"(?P<ip_address>(\d{1,3}\.){3}\d{1,3})", row)
        method = re.search(r"(?P<method>GET|POST|OPTIONS|HEAD|DELETE|PUT)", row)
        duration = re.search(r"(?P<duration>\n*\d*$)", row)
        date = re.search(r"(?P<date>\s*\[[^][]*])", row)
        url = re.findall(r"(?P<url>\".*?\")", row)
        temp['ip'] = ip.group('ip_address')
        temp['duration'] = duration.group('duration')
        temp['method'] = method.group('method')
        temp['date'] = date.group('date')
        temp['url'] = url[1].replace('"', '')
        data.append(temp)
    data = sorted(data, key=lambda x: int(x['duration']), reverse=True)
    if len(data) > 3:
        return data[0:3]
    else:
        return data
        

def top_ip_addresses(res):
    """Топ 3 IP адресов, с которых было сделано наибольшее количество запросов"""
    ip_dict = {}
    for row in res:
        ip = re.search(r"(?P<ip_address>(\d{1,3}\.){3}\d{1,3})", row)
        if ip.group('ip_address') in ip_dict:
            ip_dict[ip.group('ip_address')] += 1
        else:
            ip_dict[ip.group('ip_address')] = 1
    ip_dict = sorted(ip_dict.items(), key=lambda item: item[1], reverse=True)
    if len(ip_dict) > 3:
        return ip_dict[0:3]
    else:
        return ip_dict


def get_count_methods(res):
    """Количество запросов по HTTP-методам"""
    ip_dict = {'GET': 0, 'POST': 0, 'OPTIONS': 0, 'HEAD': 0, 'DELETE': 0, 'PUT': 0}
    for row in res:
        request = re.search(r"(?P<request>GET|POST|OPTIONS|HEAD|DELETE|PUT)", row)
        ip_dict[request.group('request')] += 1
    return ip_dict


def format_result(res):
    """Сборка общего результата"""
    top_ip = top_ip_addresses(res)
    count_request = get_count_methods(res)
    duration = top_duration(res)
    info = {"top_ips": {}, "total_stat": {}, "top_longest": []}
    for ip in top_ip:
        info['top_ips'][ip[0]] = ip[1]
    for key, value in count_request.items():
        info['total_stat'][key] = value
    for value in duration:
        info['top_longest'].append(value)
    info["total_requests"] = len(res)
    return info


def analysis_log(path):
    """Чтение и обработка логов, запись в json"""
    if os.path.isdir(path):
        for file_name in os.listdir(path):
            basename, extension = os.path.splitext(file_name)
            if extension == '.log':
                with open(os.path.join(path, file_name), "r") as file:
                    res = [row for row in file]
                    info = format_result(res)
                    write_and_print_log_analysis(info, file_name)
    elif os.path.isfile(path):
        with open(path, "r") as file:
            res = [row for row in file]
            info = format_result(res)
            write_and_print_log_analysis(info, path.split("/")[-1])


def write_and_print_log_analysis(result, filename):
    """Запись в json файл и распечатка результата"""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open(f"{filename}_log_analysis.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)
        print(json.dumps(result, indent=4))


if __name__ == "__main__":
    analysis_log('/Users/annapogrebnik/PycharmProjects/pythonProject1/python_qa_otus/hw10')
