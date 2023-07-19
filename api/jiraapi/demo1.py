import requests
import json

# userid="mdbasheer333"
# resp = requests.get(f"https://api.github.com/users/{userid}")
# print(resp.status_code)
# print(resp.json())
# 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

# hd = {
#     "Accept": "application/vnd.github+json",
#     "Authorization": "token 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"
# }
#
# payload = {
#     "name": "Hello-World1234",
#     "description": "This is your first repo!",
#     "homepage": "https://github.com",
#     "private": False,
#     "is_template": True
# }
# resp = requests.post("https://api.github.com/user/repos", headers=hd, data=json.dumps(payload))
# print(resp.status_code)
# print(resp.json())

userid = "mdbasheer333"
repo = "Hello-World1111qsda1"

hd = {
    "Accept": "application/vnd.github+json",
    "Authorization": "token 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"
}
# payload= {
#     "description": "This is RESTTTTTTTTTTTTTTTT"
# }
# resp = requests.patch(f"https://api.github.com/repos/{userid}/{repo}", headers=hd,data=json.dumps(payload))
# print(resp.status_code)
# print(resp.json())

resp = requests.delete(f"https://api.github.com/repos/{userid}/{repo}", headers=hd)
print(resp.status_code)
try:
    resp.json()
    assert True == False
except:
    print("tc passed")

# 1. create a repo & val resp
# 2. get repo and validate
# 3. patch repo & validate
# 4. get repo and validate
# 5. delet repo & validare
# 6. get repo and validate
