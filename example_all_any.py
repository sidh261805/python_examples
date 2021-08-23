num1 = [2,4,6,8,0]
num2 = [1,3,5,6,7]

#if any True final is true
print(any([num%2==0 for num in num1]))  
print(any([num%2==0 for num in num2]))

#if all True final is true
print(all([num%2==0 for num in num1]))
print(all([num%2==0 for num in num2]))

def sum(*args):
    if all([(type(arg)==int or type(arg)==float) for arg in args]):
        return "all are int or float"
    else:
        return "different types"

print(sum(1,2,3,5.5,"hello"))

################# Advance min 0r max ###################

student = [{"name" : "sidd", "score" : 80, "age" : 27},{"name" : "alka", "score" : 90, "age" : 26},{"name" : "lala", "score" : 99, "age" : 30}]
print(max(student, key = lambda item: item.get("score")))
print(max(student, key = lambda item: item.get("score"))["name"])

################ Advance sort ############################
fruits = ['apple','kiwi','mango','banana']
fruits.sort()
print(fruits)

print(sorted(student, key= lambda dic:dic.get("name"),reverse=True))