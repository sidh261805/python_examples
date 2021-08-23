from functools import wraps
def only_data_type_allowed(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            if all ([type(arg)==data_type for arg in args]):
                return function(*args,**kwargs)
            print("Invalid arguments")
        return wrapper
    return decorator

@only_data_type_allowed(str)
def string_join(*args):
    string=''
    for arg in args:
        string += arg
    return string

print(string_join('sidd ','alka ','lala'))