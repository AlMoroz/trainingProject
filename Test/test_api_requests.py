import uuid
import pytest
import requests
from Source import requests_funcs as func

def basic_post_request(body):
    return

def basic_put_request():
    return

def basic_delete_request():
    return


def test_call_everything():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available'
    tkn = func.generate_token()
    r = func.basic_get_request(url, func.generate_header(tkn))
    print("here",r.content)

