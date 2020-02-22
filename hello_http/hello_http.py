import requests

response = requests.get("http://github.com")
print(response)
print(response.status_code)

if response.status_code == 200:
    print("succeeded")
elif response.status_code == 404:
    print("not found")
