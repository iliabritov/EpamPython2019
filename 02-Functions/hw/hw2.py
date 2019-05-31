def atom(arg=None):
    def get_value():
        return arg
    def set_value(value):
        nonlocal arg
        arg = value
        return arg
    def process_value(*functions):
        nonlocal arg
        for func in functions:
            arg = func(arg)
        return arg
    def delete_value():
        nonlocal arg, get_value, set_value, process_value, delete_value
        del arg, get_value, set_value, process_value, delete_value
    return get_value, set_value, process_value, delete_value
