import requests
import json
import random

import string


def test_get_specific_user(api_env):
    userid = "mdbasheer333"
    resp = requests.get(f"{api_env}/users/{userid}")
    print(resp.status_code)
    print(resp.json())


def test_post_crate_repo(api_env):
    hd = {
        "Accept": "application/vnd.github+json",
        "Authorization": "token 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"
    }
    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k=7))
    payload = {
        "name": f"Hello-World_From_Python {res}",
        "description": "This is your first repo!",
        "homepage": "https://github.com",
        "private": False,
        "is_template": True
    }
    print(f"{api_env}/user/repos")
    resp = requests.post(f"{api_env}/user/repos", headers=hd, data=json.dumps(payload))
    print(resp.status_code)
    print(resp.json())
