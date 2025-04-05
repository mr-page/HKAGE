import os
os.system('''
curl -X 'GET' \
  'http://127.0.0.1:8000/test' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=user1&password=password1&scope=&client_id=string&client_secret=string'
  ''')