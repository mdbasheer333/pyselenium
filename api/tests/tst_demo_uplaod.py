import requests


def tst_uplaod_file():
    url = 'https://httpbin.org/post'
    multiple_files = [
        ('images', ('dummy_upload.png', open('C:\\Users\RASHEED\\Desktop\\dummy_upload.png', 'rb'), 'image/png'))]
    resp = requests.post(url, files=multiple_files)
    print(resp.text)
    print(resp.json()['files']['images'])



tst_uplaod_file()
