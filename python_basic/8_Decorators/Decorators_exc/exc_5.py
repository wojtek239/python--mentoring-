import time


def timethis(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"execution time of {func.__name__}: {execution_time} seconds")
        return result

    return wrapper


@timethis
def example_function():
    time.sleep(2)
    print("finished execution")

example_function
