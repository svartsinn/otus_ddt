import requests


def test_status_code_by_url(params):
    response = requests.get(params['url'])
    assert response.status_code == int(params['status_code'])
