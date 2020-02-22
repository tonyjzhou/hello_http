import requests
from requests import HTTPError


def http_headers(url: str):
    try:
        response = requests.get(url)
        print(response.headers)
        for k, v in response.headers.items():
            print(f"{k} => {v}")
    except HTTPError as e:
        print(f"{e}")
    else:
        print(f"{url} succeeded")


http_headers("https://api.github.com")
