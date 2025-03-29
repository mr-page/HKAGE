import requests
response = requests.get('http://127.0.0.1:8000/protected', auth=('user1', 'password1'))
print(response.json())
