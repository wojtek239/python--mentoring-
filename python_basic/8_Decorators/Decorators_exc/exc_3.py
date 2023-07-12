def count(func):
    count_dict = {}

    def wrapper(*args, **kwargs):
        nonlocal count_dict
        count_dict[func.__name__] = count_dict.get(func.__name__, 0) + 1
        result = func(*args, **kwargs)
        return result

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper
