import inspect

def modified_func(func, *fixated_args, **fixated_kwargs):

    #def new_func(*args, **kwargs):
        
    return new_func


def func_var(func):
    """ get all named variable from function """
    def_fc = inspect.getsourcelines(func)[0][0]
    def_fc = def_fc[def_fc.index('(') + 1 : def_fc.index(')')]
    def_fc = def_fc.replace(',', '').split()
    named_var = []
    for elem in def_fc:
        if '=' in elem:
            named_var.append(elem.split('=')[0])
    return named_var



def fc1(a, b):
    return a + b
def fc2(a, b, c=4):
    return a*b*c
def fc3():
    print('Useless fc!')
def fc4(a=1, b=2, c=3):
    return a ** b ** c



print(func_var(fc1))
print(func_var(fc2))
print(func_var(fc3))
print(func_var(fc4))
    
