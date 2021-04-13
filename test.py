import requests
import json

key = "avatar"
res = requests.get("https://reqres.in/api/users?page=2")
resolved = res.json()
resolved_txt = res.text
#print(resolved)
if (resolved_txt.find(key) == -1):
    print("Not found")
else:
    print("Found")
    with open('personal.json', 'w') as json_file:
         json.dump(resolved, json_file)