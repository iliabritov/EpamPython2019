import functools


def print_result(func):
    @change_info(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result 
    return wrapper


def change_info(req_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.__name__ = req_func.__name__
        wrapper.__doc__ = req_func.__doc__
        wrapper.__original_func = req_func
        return wrapper
    return decorator


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == '__main__':
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    without_print = custom_sum.__original_func
    custom_sum.__original_func
    # the result returns without printing
    without_print(1, 2, 3, 4)
