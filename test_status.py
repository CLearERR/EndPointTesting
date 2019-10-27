# TODO: 5 видов запросов
import requests
import json
import pytest
from getparams import get_url

@pytest.mark.status
@pytest.mark.usefixtures("ini")
@pytest.mark.parametrize("code", [418])
def test_get_status(ini, code):
    resp = requests.get(str(get_url(ini) + '/status/' + code))
    print(resp.status_code)
    print(resp.text)
    assert resp.status_code == 200, "Wrong status code of response."