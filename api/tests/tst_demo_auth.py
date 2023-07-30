import requests

from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth


def basic_auth_demo():
    basic = HTTPBasicAuth('user', 'pass')
    # resp = requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)
    resp = requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)
    print(resp.headers)
    print(resp.status_code)
    print(resp.json())


def basic_digestive_demo():
    basic = HTTPBasicAuth('user', 'pass')
    url = 'https://httpbin.org/digest-auth/auth/user/pass'
    resp = requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
    print(resp.headers)
    print(resp.status_code)
    print(resp.json())


basic_digestive_demo()

# https://developer.paypal.com/api/rest/authentication/
# https://requests.readthedocs.io/en/latest/