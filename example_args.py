# *operator
# *args

def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum(1,2,3,4))
print(sum())
lis = [2,3,4,5]
print(sum(*lis))   #pass list

def mixed(num1,num2,*args):  #(*args,num) not possible
    total = 0
    for num in args:
        total += num
    sum2 = num1 + num2
    return total,sum2

print(mixed(1,2,1,2,3,4))

def cube(num2,*args):  #(*args,num) not possible
    return [num**num2 if(args) else "pass value" for num in args]
    # total = []
    # if args != 0:
    #     for num in args:
    #         total.append(num**num2) 
    #     return total
    # else:
    #     print("pass value")
numb = [1,2,3]
print(cube(3,*numb))


#**kwargs (keyword argument)
def func(**kwargs):
    print(kwargs)
    for i,j in kwargs.items():
        print(f"{i} : {j}")

func(first_name = "sidd", last_name = "dhakad")
d = {"first_name" : "alka", "last_name" : "lala","age" : 27}
func(**d)

# order(name,*args,name="sidd",**kwargs)  ==> imp PADK