import pytest


def pytest_addoption(parser):
    parser.addoption('--url',
                     default='https://ya.ru',
                     help='Specify target URL')
    parser.addoption('--status_code',
                     default=200,
                     help='Specify target status code')


@pytest.fixture
def params(request):
    params = {}
    params['url'] = request.config.getoption('--url')
    params['status_code'] = request.config.getoption('--status_code')
    if params['url'] is None or params['status_code'] is None:
        pytest.skip()
    return params
