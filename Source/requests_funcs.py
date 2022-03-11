import requests
import uuid
import urls

def generate_token():
    return str(uuid.uuid4())


def generate_header(token):
    header_data = dict()
    header_data.setdefault('accept', 'application/json')
    header_data.setdefault('Content-Type', 'application/json; charset=utf-8')
    header_data.setdefault('Authorization', token)
    return header_data


def basic_get_request(url, auth_header):
    r = requests.get(
        url=url,
        headers=auth_header,
    )
    return r
