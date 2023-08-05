# client id:
# secret ket:
import requests
from requests.auth import HTTPBasicAuth


def other_demo_tst():
    basic = HTTPBasicAuth("",
                          "")
    hd = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {

        "grant_type": "client_credentials"
    }
    resp = requests.post("https://api-m.sandbox.paypal.com/v1/oauth2/token", auth=basic, headers=hd, data=payload)
    at = resp.json()['access_token']
    print(resp.json()['access_token'])
    print(resp.json()['token_type'])
    print(resp.json()['expires_in'])

    headers = {
        'Authorization': f'Bearer {at}',
        'Content-Type': 'application/json',
    }
    params = (
        ('total_required', 'true'),
    )
    response = requests.get('https://api-m.sandbox.paypal.com/v2/invoicing/invoices', headers=headers, params=params)
    print(response.status_code)
    print(response.json())


other_demo_tst()
