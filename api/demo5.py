import requests

# resp = requests.get("https://www.google.com/search?q=selenium")
# print(resp.cookies.items())

user_id = 2
resp = requests.get(f"https://reqres.in/api/users?delay=3", timeout=50)
print(resp.elapsed)
