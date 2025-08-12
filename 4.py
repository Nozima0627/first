import json
f = open("first/users.json")
data = json.load(f)
lst = []
for i in data:
    if i["is_active"] == True:
       lst.append(i["age"])
avg = sum(lst)/len(lst)
print("is_active foydalanuvchilarning o`rtacha yoshi")
print(int(avg))