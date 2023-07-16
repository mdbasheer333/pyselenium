import requests

# resp = requests.get("https://www.google.com/search?q=selenium")
# print(resp.cookies.items())

user_id=2
resp = requests.get(f"https://reqres.in/api/users/{user_id}")
print(resp.json())
print(resp.headers)
print(resp.request.headers)