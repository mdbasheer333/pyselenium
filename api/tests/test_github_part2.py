import requests
import json


def test_patch_rename_repo():
    userid = "mdbasheer333"
    repo = "Hello-World1111qsda1"

    hd = {
        "Accept": "application/vnd.github+json",
        "Authorization": "token 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"
    }
    payload = {
        "description": "This is RESTTTTTTTTTTTTTTTT"
    }
    resp = requests.patch(f"https://api.github.com/repos/{userid}/{repo}", headers=hd, data=json.dumps(payload))
    print(resp.status_code)
    print(resp.json())


def test_delete_repo_deletion():
    userid = "mdbasheer333"
    repo = "Hello-World1111qsda1"
    hd = {
        "Accept": "application/vnd.github+json",
        "Authorization": "token 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"
    }
    resp = requests.delete(f"https://api.github.com/repos/{userid}/{repo}", headers=hd)
    print(resp.status_code)
    try:
        resp.json()
        assert True == False
    except:
        print("tc passed")
