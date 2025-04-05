import os
os.system('''
curl -X 'POST' \
  'https://instantly-beloved-griffon.ngrok-free.app/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=user1&password=password1&scope=&client_id=string&client_secret=string'
  ''')