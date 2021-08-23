def fabonacci_seq(n):
    ''' calculate fabonaicc series '''
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b)
    else:
        print(a,b, end=" ")
        for i in range(n-2):
            c= a+b
            a=b
            b=c
            print(b, end = " ")

fabonacci_seq(10)

x = 9
def user(name='unknown',age=None):
    # global x = 7
    print(f"name {name} and age {age}")
user()
user("sidd")
user("sidd",28)

print(fabonacci_seq.__doc__)
print(fabonacci_seq.__name__)
print(help(fabonacci_seq))