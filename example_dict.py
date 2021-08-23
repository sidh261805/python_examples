#undodered collection data
user = {"name" : "sidd","age" : "27"}
print(user)
user1 = dict(name = "sidd",age=27)
print(user1)

print(user1["name"])

user2 = {}
user2["name"] = "sidd"
user2["age"] = 24
print(user2)

if 'name' in user:
    print("present")
if 'sidd' in user.values():   #dict value
    print("present")

for i in user.keys():
    print(i)

user_item = user.items()
print(type(user_item))
print(user_item)

for key,value in user.items():
    print(f"key {key} value {value}")

print(user.pop("name"))  #user.popitem() random pop
print(user)

user["name"] = "sidd"
print(user)

user4 = {"name" : "alka","song" : "lala"}

user.update(user4)  #update name if key is same
print(user)

d = dict.fromkeys(("name","age","height"), "None")
print(d)

print(d.get("name"))
print(d.get("namess"))
print(d.get("namess", " not found !!"))
d.clear()

d = dict.fromkeys(["name","age","height"], "None")
print(d)

d1 = d.copy()

d = dict.fromkeys(("abc"), "None")
print(d)