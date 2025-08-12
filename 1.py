import json
f = open("first/users.json")
data = json.load(f)
print("Pythonni biladigan foydalanuvchilar: ")
for data in data:
    for v in data["skills"]:
        if v == "Python":
            print(data["name"])