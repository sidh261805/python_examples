i = 1
while i<=4:
    print("hello")
    i += 1

name = "siddharth dhakad"
i = 0
temp_var = ""
while i < len(name):
    if name[i] not in temp_var:
        print("# {} : {}".format(name[i],name.count(name[i])))
        temp_var += name[i]
    else:
         pass
    i += 1

temp_var = ""
for i in range(len(name)):
    if name[i] not in temp_var:
        print("# {} : {}".format(name[i],name.count(name[i])))
        temp_var += name[i]
    else:
         pass
    i += 1

for i in range(1,11,2):
    print(i)

for i in range(10,-1,-2):
    print(i)