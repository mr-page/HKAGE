import requests
data = {'grant_type':'password','username':'user1','password':'password1','scope':'','client':'string','client_secret':'string'}
response = requests.post('http://127.0.0.1:8000/token', data)
print(response.json()['access_token'])
access_token = response.json()['access_token']
