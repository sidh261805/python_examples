
fun = lambda s : True if len(s) > 5 else False
print(fun("sidd"))
print(fun("sidddha"))

names = ['alka','sidd','lala']
for pos,name in enumerate(names):
    print(f"{pos} ===> {name}")

string = "lala"
for pos,name in enumerate(names):
    if(name == string):
        print(f"{pos} ===> {name}")