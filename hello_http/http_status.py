import requests
from requests import HTTPError


def http_status(urls: list):
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as e:
            print(f"{e}")
        else:
            print(f"{url} succeeded")


http_status(["http://github.com", "http://yahoo.com/invalid123"])
