import requests

# resp = requests.get("https://reqres.in/api/users?page=2")

qp = {"page": 2}
resp = requests.get("https://reqres.in/api/users", params=qp)
print(resp.url)
print(resp.json())

