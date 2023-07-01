import json


def tst_read_json():
    with open("sample.json", 'r') as json_file:
        data = json.load(json_file)
        # print(data)
        print(data['name'])
        print(data['age'])
        print(data['dob'])
        print(data['languegess'])


tst_read_json()
