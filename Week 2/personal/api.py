import requests

response = requests.get('https://my-json-server.typicode.com/typicode/demo/posts')

print(response.json())