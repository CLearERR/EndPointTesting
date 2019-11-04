"""
.. module:: test_redirect
   :synopsis: All redirect tests are defined here
.. moduleauthor:: Dmitry Berdov <https://github.com/CLearERR>
"""


import requests
import pytest
import allure
import logging
from getparams import get_url


@allure.title("redirect")
@allure.suite("1.0.0")
@allure.feature("getredirect")
@pytest.mark.redirect
@pytest.mark.positive
@pytest.mark.usefixtures("ini")
@pytest.mark.parametrize("count", ["1", "2", "10", "20", "29", "30",
                                   pytest.param("-1", marks=pytest.mark.xfail),
                                   pytest.param("0", marks=pytest.mark.xfail),
                                   pytest.param("31", marks=pytest.mark.xfail),
                                   pytest.param("", marks=pytest.mark.xfail),
                                   pytest.param("NaN", marks=pytest.mark.xfail)])
def test_get_redirect(ini, count):
    """
        **test_get_redirect**

        This checks different scenarios about getting request redirects.

        Expected result: 200 status-code and correct number of redirections.

        Available parameters sets:
        1 - 6) Positive parameters
        7 - 11) Simulation: we suppose (just for example, it is obviously wrong) that these parameters should be valid,
        but now they fail test.

        Pytest marks: "redirect", "positive"
    """
    logging.info("Count: {}".format(count))
    resp = requests.get(str(get_url(ini) + '/redirect/' + str(count)))
    logging.info("Response: {}".format(resp.text))
    assert resp.status_code == 200, "Wrong status code of response."
    assert len(resp.history) == int(count), "Wrong redirection number."


@allure.title("redirect")
@allure.suite("1.0.0")
@allure.feature("postredirect")
@pytest.mark.redirect
@pytest.mark.negative
@pytest.mark.usefixtures("ini")
@pytest.mark.parametrize("count", ["1"])
def test_post_redirect(ini, count):
    """
        **test_post_redirect**

        This checks negative scenario about POST request redirect.

        Expected result: 405 status-code.

        Pytest marks: "redirect", "negative"
    """
    logging.info("Count: {}".format(count))
    resp = requests.post(str(get_url(ini) + '/redirect/' + count))
    logging.info("Response: {}".format(resp.text))
    assert resp.status_code == 405, "Wrong status code of response."