import requests
import json
#
#
# def test_patch_rename_repo(api_env):
#     userid = "mdbasheer333"
#     repo = "Hello-World_From_Python"
#
#     hd = {
#         "Accept": "application/vnd.github+json",
#         "Authorization": "token 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"
#     }
#     payload = {
#         "description": "This is RESTTTTTTTTTTTTTTTT"
#     }
#     resp = requests.patch(f"{api_env}/repos/{userid}/{repo}", headers=hd, data=json.dumps(payload))
#     print(resp.status_code)
#     print(resp.json())
#
#
# def test_delete_repo_deletion(api_env):
#     userid = "mdbasheer333"
#     repo = "Hello-World_From_Python"
#     hd = {
#         "Accept": "application/vnd.github+json",
#         "Authorization": "token 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"
#     }
#     resp = requests.delete(f"{api_env}/repos/{userid}/{repo}", headers=hd)
#     print(resp.status_code)
#     try:
#         resp.json()
#         assert True == False
#     except:
#         print("tc passed")
