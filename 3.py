import json
f = open("first/users.json")
data = json.load(f)
for i in data:
    if i["is_active"] == True:
       print(i["name"])