import requests

request_url = "https://todolist.example.com/tasks/"
response = requests.get(request_url)

if response.status_code == 200:
    print(response)
else:
    raise Exception(f"GET /tasks/ {response.status_code}")
