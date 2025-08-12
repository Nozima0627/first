import json
f = open("first/users.json")
data = json.load(f)
max_yosh = 0
for i in data:
    if i["age"] > max_yosh:
        max_yosh = i["age"]
print("Yoshi katta foydalanuvchilar:")
for i in data:
    if max_yosh == i["age"]:
        print(f"Ismi: {i["name"]}\nKasbi:{i["profession"]}\nYoshi: {max_yosh}")
        print()