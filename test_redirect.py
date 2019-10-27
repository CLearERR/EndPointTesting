import requests
import json
import pytest
from getparams import get_url


@pytest.mark.redirect
@pytest.mark.usefixtures("ini")
@pytest.mark.parametrize("count", ["1", "2", "10", "20", "29", "30",
                                   pytest.param("-1", marks=pytest.mark.xfail),
                                   pytest.param("0", marks=pytest.mark.xfail),
                                   pytest.param("31", marks=pytest.mark.xfail),
                                   pytest.param("", marks=pytest.mark.xfail),
                                   pytest.param("NaN", marks=pytest.mark.xfail)])

def test_get_redirect(ini, count):
    # convert dict to json by json.dumps() for body data.
    # resp = requests.post(url, data=json.dumps(payload, indent=4))
    resp = requests.get(str(get_url(ini) + '/redirect/' + count))

    print(resp)
    # Validate response headers and body contents, e.g. status code.
    print(resp.status_code)
    print(resp.text)

    assert resp.status_code == 200, "Wrong status code of response."
    resp_body = resp.json()

@pytest.mark.redirect
@pytest.mark.negative
@pytest.mark.usefixtures("ini")
@pytest.mark.parametrize("count", ["1"])
def test_post_headers(ini, count):
    resp = requests.post(str(get_url(ini) + '/redirect/' + count))
    print(resp.status_code)
    print(resp.text)
    assert resp.status_code == 405, "Wrong status code of response."