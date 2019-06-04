import inspect


def modified_func(func, *fixated_args, **fixated_kwargs):
    def new_func(*fixed_args, **fixed_kwargs):
        frame = inspect.currentframe()
        args = inspect.getargvalues(frame)[3]
        code = inspect.getsource(func)
        func_name = code[4:code.index('(')]
        docs = [('A func implementation of ' + func_name + '\n'),
                'with pre-applied arguments being:\n',
                ('fixated_args: ' + str(args['fixated_args']) + '\n'),
                ('fixated_kwargs: ' + str(args['fixated_kwargs']) + '\n'),
                ('code: \n' + code)]
        new_func.__doc__ = ''.join(docs)
        new_func.__name__ = 'func_' + func_name
        sum_args = [*fixated_args, *fixed_args]
        sum_kwargs = {**fixated_kwargs, **fixed_kwargs}
        return func(*sum_args, **sum_kwargs)
    return new_func
