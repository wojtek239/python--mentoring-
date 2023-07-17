import time
from datetime import datetime


def timethis(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = round(end_time - start_time, 4)
        print(f"execution time of {func.__name__}: {execution_time} seconds")
        return result

    return wrapper


@timethis
def example_function():
    time.sleep(2)
    print("finished execution")


example_function()
