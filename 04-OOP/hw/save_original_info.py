import functools


def print_result(func):
    def decorator(req_func):
        req_func.__doc__ = func.__doc__
        req_func.__name__ = func.__name__
        req_func.__original_func = func
        return req_func

    @decorator
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper


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
