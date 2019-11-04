import pytest
import time
import os
import logging
import datetime

def pytest_configure(config):
    config.addinivalue_line("markers", "headers")
    config.addinivalue_line("markers", "redirect")
    config.addinivalue_line("markers", "status")
    config.addinivalue_line("markers", "positive")
    config.addinivalue_line("markers", "negative")
    config.addinivalue_line("markers", "explicit")
    config.addinivalue_line("markers", "timeout")



def pytest_addoption(parser):
    parser.addoption('--ini', action='store', default='config.ini')

@pytest.fixture(scope="session")
def ini(request):
    return os.path.join(os.path.dirname(__file__), request.config.getoption('--ini'))

@pytest.fixture(scope="function", autouse=True)
def set_log(caplog):
    caplog.set_level(logging.INFO)
    logging.info("==========start logging==========")
    yield
    logging.info("==========end logging==========")
