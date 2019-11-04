"""
.. module:: test_headers
   :synopsis: All headers tests are defined here
.. moduleauthor:: Dmitry Berdov <https://github.com/CLearERR>
"""


import requests
import pytest
import allure
import logging
from getparams import get_url


@allure.title("headers")
@allure.suite("1.0.0")
@allure.feature("getheaders")
@pytest.mark.headers
@pytest.mark.positive
@pytest.mark.usefixtures("ini")
@pytest.mark.parametrize("headers_add", [{},
                                         {'Content-Type': 'application/json'},
                                         {'Referer': 'https://httpbin.org/', 'Sec-Fetch-Mode': 'cors'},
                                         {'Accept': ''},
                                         {'User-Agent': '', 'Sec-Fetch-Mode': 'cors'}])
def test_get_headers(headers_add, ini):
    """
        **test_get_headers**

        This checks different positive scenarios about getting request headers.

        Expected result: 200 status-code and correct list of headers.

        Available parameters sets:
        1) Empty header list
        2) 1 Non-default header
        3) 2 Non-default headers
        4) 1 default header
        5) 1 default header and 1 non-default header

        Pytest marks: "headers", "positive"
    """
    headers_default = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "Host": "httpbin.org",
                       "User-Agent": "python-requests/2.22.0"}
    headers_unite = {**headers_default, **headers_add}
    logging.info("Headers for addition: {}".format(headers_add))
    logging.info("Headers default: {}".format(headers_default))

    resp = requests.get(str(get_url(ini) + '/headers'), headers=headers_add)

    logging.info("Response: {}".format(resp.text))

    assert resp.status_code == 200, "Wrong status code of response."
    resp_body = resp.json()['headers']
    for key in headers_unite:
        assert key in resp_body, "Header key from request doesn't exist in response."
        assert str(resp_body[key]) == str(headers_unite[key]), "Wrong value of key in response."


@allure.title("headers")
@allure.suite("1.0.0")
@allure.feature("postheaders")
@pytest.mark.headers
@pytest.mark.negative
@pytest.mark.usefixtures("ini")
@pytest.mark.parametrize("headers_add", [{'Content-Type': 'application/json'}])
def test_post_headers(headers_add, ini):
    """
        **test_post_headers**

        This checks negative scenario (unsupported operation "POST").

        Expected result: 405 status-code

        Pytest marks: "headers", "negative"
    """
    resp = requests.post(str(get_url(ini) + '/headers'), headers=headers_add)
    logging.info("Response: {}".format(resp.text))
    assert resp.status_code == 405, "Wrong status code of response."
