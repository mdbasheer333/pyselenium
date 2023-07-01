import json


def tst_write_json():
    dct = {
        "name": "basheer",
        "age": 30,
        "prof": "tester",
        "lang": ["telugu", "hindi", "eng"]
    }
    # myfiledata = json.dumps(dct, indent=4)
    # with open("myjson.json", 'w') as json_file:
    #     json_file.write(myfiledata)

    with open("myjson.json", 'w') as json_file:
        json.dump(dct, json_file, indent=4)


tst_write_json()
