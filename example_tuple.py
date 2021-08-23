num = (1,) #add comma not work (1)
print(type(num))
name = 'apple','mango','banana'
print(type(name))
fruit1, fruit2, fruit3 = (name)
print(fruit1)

fruits = ('apple',['mango','banana'])
fruits[1].pop()
fruits[1].append("kiwi")
print(fruits)
print(len(fruits))
print(fruits.count("apple"))



def func(int1, int2):
    add = int1+int2
    multi = int1*int2
    return add , multi

add , mul = func(2,3)
print(f"add : {add} and multiple : {mul}")

num = tuple(range(1,11))