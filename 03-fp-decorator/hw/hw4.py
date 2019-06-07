import time
from threading import Timer

cache = []


def make_cache(hold_time):
    def decorator(func):
        
        def deleter():
            del cache[0]

        def mem_func(*args, **kwargs):
            result = func(*args, **kwargs)
            cache.append(result)
            Timer(hold_time, deleter).start()
            return result
        
        return mem_func
    return decorator


@make_cache(30)
def authorization():
    """put in cache user name and password"""
    
    user_name = input('Give me user name: ')
    password = input('Give me password: ')
    return (user_name, password)
    

def usefull_func(args: list):
    return ' '.join(args)


def access_to_func(func, data):
    if cache: 
        if cache[0][0] == 'admin' and cache[0][1] == 'qwerty':
            print('Access granted!')
            result = func(data)
            print(f"Your result: {result}")
            return result
    print('''\nAccess denied
Your session time is over,
or you give me uncorrect login and password.
Please, try again\n''')
    authorization()


if __name__ == '__main__':
    # we request access to function several times..
    # if we wanna work with functions, we need to be authorized
    # user name: admin, password: qwerty
    authorization()
    g = access_to_func(usefull_func, ['1','2','3','4'])
    time.sleep(15) # waiting....
    g = access_to_func(usefull_func, ['eggs', 'and', 'bacon'])
    time.sleep(20) # sleepeing
    g = access_to_func(usefull_func, ['and', 'another', 'try'])
    g = access_to_func(usefull_func, ['and', 'another', 'try'])            


    
    
