import requests


def checkWebsite(website):
    url = website
    surl = autoNameCheck(url)
    r = requests.get(surl)
    if r.status_code == 200:
        print("Your website is live")
    else:
        print("Webiste it down with status code" + r.status_code)

# Lets try to make a function which will analyse


def autoNameCheck(url):
    surl = str(url)
    if surl.startswith("www"):
        surl = "https://"+surl
    return surl


print("This is a function which will return true if website is live")

# This is when url is provided with correct schema i.e https://
checkWebsite("www.semdoctors.com")
