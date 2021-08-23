fruits = ["apple","mango",1,2,3,4.0]
print(fruits)
fruits[2:] = "tox"
print(fruits)
fruits[2:] = ["kiwi","banana"]
print(fruits)
fruits.append("cherry")
print(fruits)
fruits.insert(1,'grapes')
print(fruits)

fruits1 = ["kiwi","banana"]
fruits2 = ["apple","mango"]
print(fruits1 + fruits2)

fruits1.extend(fruits2)
print(fruits1)


fruits1.append(fruits2)
print(fruits1)

del fruits1[1]
print(fruits1)
fruits1.pop()
print(fruits1)
fruits1.pop(2)
print(fruits1)
fruits1.remove("kiwi")
print(fruits1)

number = [3,5,6,1,8,9]

for i in range(len(number)-1):
    for j in range(len(number)-1):
        if number[j] > number [j+1]:
            temp = number[j+1]
            number[j+1] =  number[j]
            number[j] = temp

print(number)

fruit = ['apple', 'grapes', 'mango', 'kiwi', 'banana', 'cherry','apple']
print(fruit.count("apple"))
print(fruit.sort())
print(sorted(fruit)) #not sort in list only print

fruit_copy = fruit.copy()
print(fruit_copy)

fruit.clear()
print(fruit)



def takeSecond(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key=takeSecond)
print('Sorted list:', random)

fruit1 = ['apple', 'grapes', 'mango', 'kiwi', 'banana', 'cherry','apple']
fruit2 = ['apple', 'grapes', 'mango', 'kiwi', 'banana', 'cherry','apple']
print(fruit1 == fruit2) #check value
print(fruit1 is fruit2) #check memory

userinfo = ["sidd","dhakad","24"]
print(",".join(userinfo))
print(type(userinfo))

num = list(range(1,11))
print(num.pop())
print(num.index(5))
print(num.index(5,4))


def negative_list(l):
    rt = []
    for i in l:
        rt.append(-i)
    return rt

num1 = [3,4,5,6,7]
print(negative_list(num1))
