"""
.. module:: test_status
   :synopsis: All status tests are defined here
.. moduleauthor:: Dmitry Berdov <https://github.com/CLearERR>
"""


import requests
import pytest
import allure
import logging
import time
from itertools import chain
from getparams import get_url, get_conf


def status(ini, operation, code):
    """
        **status**

        This creates request for status endpoint based on received parameters.

        :param ini: config file
        :param operation : type of operation
        :type operation : str
        :param code: status-code of request
        :type code : int
        :return: status-code of response


    """
    logging.info("Operation: {}".format(operation))
    logging.info("Code: {}".format(code))
    resp = requests.request(operation, str(get_url(ini) + '/status/' + str(code)),
                            timeout=int(get_conf(ini)["timeouts"]["timeout"]))
    logging.info("Response: {}".format(resp.request))
    logging.info("Status code: {}".format(resp.status_code))
    return resp.status_code


@allure.title("status")
@allure.suite("1.0.0")
@allure.feature("supportedcodes")
@pytest.mark.status
@pytest.mark.positive
@pytest.mark.usefixtures("ini")
@pytest.mark.parametrize("operation", ["delete", "get", "patch", "post", "put"])
@pytest.mark.parametrize("code", range(200, 1000))
def test_status_positive(ini, operation, code):
    """
        **test_status_positive**

        This checks different positive scenarios about making different operations with endpoint "status".

        Expected result: status code of response, equal to status code of request

        Available parameters sets:
        operation: ["delete", "get", "patch", "post", "put"]
        code: range(200, 1000)

        Pytest marks: "status", "positive"
    """
    assert status(ini, operation, code) == code, "Wrong status code of response."


@allure.title("status")
@allure.suite("1.0.0")
@allure.feature("timeoutcodes")
@pytest.mark.status
@pytest.mark.negative_502
@pytest.mark.timeout
@pytest.mark.usefixtures("ini")
@pytest.mark.parametrize("operation", ["delete", "get", "patch", "post", "put"])
@pytest.mark.parametrize("code", range(100, 200))
def test_status_negative_timeout(ini, operation, code):
    """
        **test_status_negative_timeout**

        This checks different negative scenarios about receiving timeout exception for different operations
        with endpoint "status".

        Expected result: raise Timeout exception

        Available parameters sets:
        operation: ["delete", "get", "patch", "post", "put"]
        code: range(100, 200)

        Pytest marks: "status", "negative_502", "timeout"
    """
    with pytest.raises(requests.Timeout):
        status(ini, operation, code)


@allure.title("status")
@allure.suite("1.0.0")
@allure.feature("badgatewaycodes")
@pytest.mark.status
@pytest.mark.negative
@pytest.mark.usefixtures("ini")
@pytest.mark.parametrize("operation", ["delete", "get", "patch", "post", "put"])
@pytest.mark.parametrize("code", chain(range(0, 100), [1001, -1]))
def test_status_negative_502(ini, operation, code):
    """
        **test_status_negative_502**

        This checks different negative scenarios about making operations for "invalid" codes with endpoint "status".

        Expected result: status code 502

        Available parameters sets:
        operation: ["delete", "get", "patch", "post", "put"]
        code: range(0, 100) , 1001, -1

        Pytest marks: "status", "negative"
    """
    assert status(ini, operation, code) == 502, "Wrong status code of response."



