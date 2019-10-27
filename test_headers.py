import requests
import json
import pytest
from getparams import get_url

@pytest.mark.headers
@pytest.mark.usefixtures("ini")
@pytest.mark.parametrize("headers_add", [{},
                                         {'Content-Type': 'application/json'},
                                         {'Referer': 'https://httpbin.org/', 'Sec-Fetch-Mode': 'cors'},
                                         {'Accept': ''},
                                         {'User-Agent': '', 'Sec-Fetch-Mode': 'cors'}])
def test_get_headers(headers_add, ini):
    # url = 'https://httpbin.org/headers'
    headers_default = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "Host": "httpbin.org",
                       "User-Agent": "python-requests/2.22.0"}

    headers_unite = {**headers_default, **headers_add}

    # TODO: перебрать всевозможные headers (создание новых, отсутствие дублей стандартных, перезапись стандартных)
    # Additional headers.
    # headers_dict = {'Content-Type': 'application/json', 'accept': ''}
    # headers = {'accept': ''}
    # headers = {}

    # Body
    # payload = {'key1': 1, 'key2': 'value2'}
    # payload = {}

    # convert dict to json by json.dumps() for body data.
    # resp = requests.post(url, data=json.dumps(payload, indent=4))
    resp = requests.get(str(get_url(ini) + '/headers'), headers=headers_add)

    print(resp)
    # Validate response headers and body contents, e.g. status code.
    print(resp.status_code)
    print(resp.text)

    assert resp.status_code == 200, "Wrong status code of response."
    resp_body = resp.json()['headers']
    for key in headers_unite:
        assert key in resp_body, "Header key from request doesn't exist in response."
        assert str(resp_body[key]) == str(headers_unite[key]), "Wrong value of key in response."

    # for key in resp_body['headers']:
    #    if key in headers_add:
    #        if key in headers_default:
    #            assert

    # assert resp_body['url'] == url

    # print response full body as text

@pytest.mark.headers
@pytest.mark.negative
@pytest.mark.usefixtures("ini")
@pytest.mark.parametrize("headers_add", [{'Content-Type': 'application/json'}])
def test_post_headers(headers_add, ini):
    resp = requests.post(str(get_url(ini) + '/headers'), headers=headers_add)
    print(resp.status_code)
    print(resp.text)
    assert resp.status_code == 405, "Wrong status code of response."

def test_post_headers_body_json():
    url = 'https://httpbin.org/post'

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {'key1': 1, 'key2': 'value2'}

    # convert dict to json by json.dumps() for body data.
    resp = requests.post(url, data=json.dumps(payload, indent=4))

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['url'] == url

    # print response full body as text
    print(resp.text)