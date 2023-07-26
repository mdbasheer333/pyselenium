import requests
import json


class JiraApi:

    def __init__(self):
        self.resp = None
        self.header = {
            "Accept": "application/vnd.github+json",
            "Authorization": "token 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"
        }

    def getGitUser(self, api_env, userid):
        self.resp = requests.get(f"{api_env}/users/{userid}")
        return self.resp

    def verifyUser(self, userid):
        act_userid = self.resp.json()['login']
        assert act_userid == userid, f'login mismatch exp {userid} act is {act_userid}'
        print(f'login matching exp {userid} act is {act_userid}')

    def createUser(self, api_env, payload):
        self.resp = requests.post(f"{api_env}/user/repos", headers=self.header, data=json.dumps(payload))
        return self.resp

    def verifyRepoName(self, exp_repo_name):
        act = self.resp.json()['name']
        assert act == exp_repo_name, f'actual {act} and exp is {exp_repo_name}'
