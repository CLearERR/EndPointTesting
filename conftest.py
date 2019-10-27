import pytest
import time
import os

def pytest_configure(config):
    config.addinivalue_line("markers", "headers")
    config.addinivalue_line("markers", "redirect")
    config.addinivalue_line("markers", "status")
    config.addinivalue_line("markers", "positive")
    config.addinivalue_line("markers", "negative")
    config.addinivalue_line("markers", "get")
    config.addinivalue_line("markers", "post")


def pytest_addoption(parser):
    parser.addoption('--ini', action='store', default='config.ini')

@pytest.fixture(scope="session")
def ini(request):
    return os.path.join(os.path.dirname(__file__), request.config.getoption('--ini'))
'''
@pytest.fixture(scope="function", autouse=True)
def set_log(caplog):
    caplog.set_level(logging.INFO)
    logging.info("start logging")
    yield
    logging.info("end logging")
'''

@pytest.fixture(scope="function", autouse=True)
def set_time():
    time.sleep(1)
    yield
    time.sleep(1)