import requests
from requests import HTTPError


def http_content(urls: list):
    for url in urls:
        try:
            response = requests.get(url)
            print(response.content)
            print(response.text)
            print(response.json())
        except HTTPError as e:
            print(f"{e}")
        else:
            print(f"{url} succeeded")


http_content(["https://api.github.com"])
