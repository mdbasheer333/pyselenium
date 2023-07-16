import requests

hd = {
    "Content-Type": "application/json; charset=utf-8",
    "name": "basheer"
}
resp = requests.get("https://reqres.in/api/users?page=2", headers=hd)
print(resp.headers)
print(resp.request.headers)
print(resp.json())
