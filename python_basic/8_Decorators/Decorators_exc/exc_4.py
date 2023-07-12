def type_check(expected_type):
    def decorator(func):
        def wrapper(arg):
            if isinstance(arg, expected_type):
                return func(arg)
            else:
                print(f"Expected type {expected_type.__name__}, but received "
                      f"{type(arg).__name__}")

        return wrapper

    return decorator


@type_check(int)
def example(num):
    print(f"Received number: {num}")


example(5)
example("hello")
example(7.1)
example(True)
#?