# age = 10
# name = "basheer"
# lst = [1, 2, 3]
# print(f"name is {name} and age is {age} and num is {lst}")
# print("name is {1} and age is {0}".format(name, age))

import requests

r = requests.get("https://reqres.in/api/users?page=2")
print(r.status_code)
print(r.text)
