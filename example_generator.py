# At a time one number store in memory
# similar to list but save memory
#list for use data multiple time but generator only for one
def even_generator(n):
    for num in range(1,n+1):
        if num%2 == 0:
            yield(num)

for num in even_generator(20):
    print(num)


square = (i**2 for i in range(1,11)) # replace [] => ()

print(square)
print(next(square))
print(next(square))
print(next(square))