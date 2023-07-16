import requests

payload = {
    "name": "morpheus",
    "job": "leader"
}
resp = requests.post("https://reqres.in/api/users", data=payload)
print(resp.status_code)
print(resp.json())
print(resp.json()['id'])
id = resp.json()['id']
act_name = resp.json()['name']
exp_name = payload['name']
assert exp_name == act_name, 'name mismatching'
assert resp.json()['name'] == payload['name'], 'name mismatching'

resp = requests.delete(f"https://reqres.in/api/users/{id}")
print(resp.status_code)
assert resp.status_code == 204
