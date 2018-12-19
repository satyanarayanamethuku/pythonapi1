"""import json
import requests
url='http://127.0.0.1:8000/cookie/studentapi'
response=requests.get(url)
d=(response.json())
print(d)"""


"""import requests
url='http://127.0.0.1:8000/cookie/studentapi'
data=requests.get(url).json()
#print(data)
for p in data:
    print('Name:',p['username'])
    print('Email:',p['email'])
    print('Password:',p['password'])
    print()"""


import requests
url='http://127.0.0.1:8000/cookie/contactapi'
data=requests.get(url).json()
print(data)

for x in data:
    print('Firstname:',x['Firstname'])
