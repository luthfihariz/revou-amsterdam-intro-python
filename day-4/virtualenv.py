import requests


response = requests.get("https://reqres.in/api/users?page=1")

print(response.status_code)
print(response.json())
