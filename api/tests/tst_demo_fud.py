import requests


def tst_download_file():
    hd = {
        "accept": "image/jpeg"
    }
    rsp = requests.get("https://httpbin.org/image/jpeg", headers=hd)
    print(rsp.status_code)
    print(rsp.content)
    with open("dummy.png", "wb") as img:
        img.write(rsp.content)
    print("file is creared")


tst_download_file()
