numb = [1,2,3,4,5]
square = list(map(lambda x:x**2,numb))
print(square)

names = ['siddharth','meenakshi','lala']
length = map(len,names)
for i in length:
    print(i)

### map or filter object iterate only once
###########  FILTER FUNCTION ######################

def is_even(a):
    return a%2==0

number = [1,3,5,6,2,5,8,0,5,3]

evens = filter(is_even,number)

evens2 = filter(lambda x:x%2==0,number)

new_even = [i for i in number if i%2==0]

print(list(evens))
print(list(evens2))
print(list(new_even))

#####################iterator######################
number = [1,2,3,4,5] #tuple,string == iterables   
numb_iter = iter(number)
print(numb_iter)
print(next(numb_iter))
print(next(numb_iter))

squares = map(lambda a:a**2,number) # iterator
print(next(squares))
print(next(squares))