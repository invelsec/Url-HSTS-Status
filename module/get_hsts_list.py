import requests

def downloadList():
    try:
        print("HSTS List Downloading...")
        res = requests.get("https://github.com/mozilla/http-observatory/raw/master/httpobs/conf/hsts-preload.json")
    except ConnectionError:
        print("Connection Error")
    with open("hsts_list.json","w") as file:
        file.write(res.text)
        file.close()
        print("HSTS List Download Complete!")
