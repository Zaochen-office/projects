from requests import get
def reptile(url):
    try:
        d=get(url)
    except ConnectionError:
        return 0
    return d.json()