import requests
data = {'grant_type':'password','username':'user1','password':'password1','scope':'','client':'string','client_secret':'string'}
response = requests.post('https://instantly-beloved-griffon.ngrok-free.app/token', data)
print(response.json()['access_token'])
access_token = response.json()['access_token']


# Access protected endpoint
protected_response = requests.get(
    "http://localhost:8000/protected",
    headers={"Authorization": f"Bearer {access_token}"}
)
print(protected_response.json())