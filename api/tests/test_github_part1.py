import requests
import json
import random

from api.Utils.Assertions import CustomAssertion
from api.jiraapi.JiraApi import JiraApi

import string


def test_get_valid_user(api_env):
    jiraApi = JiraApi()
    userid = "mdbasheer333"
    resp = jiraApi.getGitUser(api_env, userid)
    assert resp.status_code == 200, f'status code incorrect exp 200 actual {resp.status_code}'
    jiraApi.verifyUser(userid)

    cust_assert = CustomAssertion()
    exp_dct = {
        'login': 'mdbasheer333',
        'type': 'User',
        'name': 'Basheer Mohammad333',
        'company': 'Oracle',
        'location': 'Hyderabad',
        'email': None,
        'public_repos': 23,
        'followers_url': 'https://api.github.com/users/mdbasheer333/followers'
    }
    cust_assert.soft_compare_values(exp_dct, resp.json())


# login, type, name, company, location, email, public_repos, followers_url

def test_get_invalid_user(api_env):
    jiraApi = JiraApi()
    userid = "mdbasheer333"
    resp = jiraApi.getGitUser(api_env, userid)
    assert resp.status_code == 200, f'status code incorrect exp 200 actual {resp.status_code}'
    jiraApi.verifyUser("mdbasheer")


def test_post_crate_repo(api_env):
    jiraApi = JiraApi()

    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k=7))
    payload = {
        "name": f"Hello-World_From_Python{res}",
        "description": "This is your first repo!",
        "homepage": "https://github.com",
        "private": False,
        "is_template": True
    }
    resp = jiraApi.createUser(api_env, payload)
    assert resp.status_code == 201, f'status code incorrect exp 201 actual {resp.status_code}'
    jiraApi.verifyRepoName(payload.get("name"))
