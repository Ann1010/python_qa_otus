import requests


def test_check_status(url, status_code):
    response = requests.get(url)
    assert response.status_code == int(status_code), \
        f"Actual value: {response.status_code}, expected: {int(status_code)}"
