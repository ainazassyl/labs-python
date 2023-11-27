# Task1.1
import requests

post_id = 1
url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'

response = requests.get(url)

print(response.json())

if 400 <= response.status_code <= 499:
    print(f"Client Error: {response.status_code}")
elif 500 <= response.status_code <= 599:
    print(f"Server Error: {response.status_code}")

