def count(func):
    count_dict = {}

    def wrapper(*args, **kwargs):
        count_dict[func.__name__] = count_dict.get(func.__name__, 0) + 1
        print(count_dict)
        result = func(*args, **kwargs)
        return result

    return wrapper


@count
def example():
    return 1


@count
def example2():
    return 0


def main():
    example()
    example()
    example()

    example2()
    example2()


if __name__ == '__main__':
    main()
