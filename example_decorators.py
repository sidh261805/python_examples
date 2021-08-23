#decorators = enhance functionality of other function
# @ use for decorator

from functools import wraps

def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        ''' this is wrapper function '''
        print('this is awesome function')
        return any_function(*args,**kwargs) 
    return wrapper_function

@decorator_function
def func1(num):
    print("inside func1 argument pass : {}".format(num))

#func1 = decorator_function(func1)
func1(7)


@decorator_function
def add(a,b):
    ''' adding two values '''
    return a+b

print(add(2,3))
print(add.__doc__)
print(add.__name__)
