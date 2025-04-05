import requests
data = {'grant_type':'password','username':'E1','password':'pw1','scope':'','client':'string','client_secret':'string'}
response = requests.post('https://instantly-beloved-griffon.ngrok-free.app/token', data)
print(response.json()['access_token'])
access_token = response.json()['access_token']


# Access protected endpoint
protected_response = requests.get(
    "https://instantly-beloved-griffon.ngrok-free.app/protected",
    headers={"Authorization": f"Bearer {access_token}"}
)
print(protected_response.json())


response = requests.get("https://instantly-beloved-griffon.ngrok-free.app/data", headers={"Authorization": f"Bearer {access_token}"})
print(response.json())