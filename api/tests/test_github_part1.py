import requests
import json


def test_get_specific_user():
    userid = "mdbasheer333"
    resp = requests.get(f"https://api.github.com/users/{userid}")
    print(resp.status_code)
    print(resp.json())


def test_post_crate_repo():
    hd = {
        "Accept": "application/vnd.github+json",
        "Authorization": "token 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"
    }

    payload = {
        "name": "Hello-World1234",
        "description": "This is your first repo!",
        "homepage": "https://github.com",
        "private": False,
        "is_template": True
    }
    resp = requests.post("https://api.github.com/user/repos", headers=hd, data=json.dumps(payload))
    print(resp.status_code)
    print(resp.json())

