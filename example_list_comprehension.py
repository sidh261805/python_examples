squares = []
for i in range(1,11):
    squares.append(i**2)

squ = [i**2 for i in range(1,11)]
print(squ)


negative = []
for i in range(1,11):
    negative.append(-i)
neg = [-i for i in range(1,11)]   #imp
print(neg)

l = ['abc','tuv','xyz']
rev = [st[::-1] for st in l]
print(rev)

even = [i for i in range(1,11) if i%2==0]
print(even)

ls = ["sss", 2,5,5.0,[3,"lsls"]]
number = [str(i) for i in ls if (type(i)==int or type(i)==float)]
print(number)

#even -> *2 || odd -> negative
number1 = [i*2 if(i%2 == 0) else -i for i in range(1,11) ]
print(number1)

square = {i:i**2 for i in range(1,5)}
print(square)

string = "siddharth"
word_count = {char:string.count(char) for char in string}
print(word_count)

odd_even = {i:("even" if i%2==0 else "odd") for i in range(1,5)}
print(odd_even)

s = {i**2 for i in range(1,5)}
print(s)