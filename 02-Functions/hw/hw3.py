def make_it_count(func, counter_name):
    def new_func(*args, **kwargs):
        globals()[counter_name] += 1
        return func(*args, **kwargs)
    return new_func


def make_it_count1(counter_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            globals()[counter_name] += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator


@make_it_count1('new1')
def jd(args):
    return ' '.join(args)


