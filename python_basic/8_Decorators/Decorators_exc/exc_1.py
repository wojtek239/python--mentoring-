def logged(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'You called {func.__name__}{args}, it returned {result}')
        return result
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


func(4, 4, 4)
