import requests

resp = requests.get("https://reqres.in/api/users?page=2")
assert resp.status_code == 200, f"status code is incorrect exp = 201 and act = {resp.status_code}"

data = resp.json()['data']

exp_data = {
    "id": 10,
    "email": "byron.fields@reqres.in",
    "first_name": "Byron",
    "last_name": "Fields",
    "avatar": "https://reqres.in/img/faces/10-image.jpg"
}

found = False
for each in data:
    if each.get("id") == exp_data.get("id"):
        assert each == exp_data, f"data mismatching exp {exp_data} and act = {each}"
        found = True
        break

assert found == True, f"record not found"
print("record is found")
