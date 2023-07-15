import requests

resp = requests.get("https://reqres.in/api/users?page=2")
assert resp.status_code == 200, f"status code is incorrect exp = 201 and act = {resp.status_code}"
# print(resp.status_code)
# print(resp.json())

data = resp.json()['data']

exp_lst = ['michael.lawson@reqres.in',
           'lindsay.ferguson@reqres.in',
           'tobias.funke@reqres.in',
           'byron.fields@reqres.in',
           'george.edwards@reqres.in',
           'rrrachel.howell@reqres.in']

act_list = []
for each_record in data:
    act_list.append(each_record['email'])
    # print(each_record['email'])

print(exp_lst)
print(act_list)

assert exp_lst == act_list, f"mismatch exp {exp_lst} and act {act_list}"
