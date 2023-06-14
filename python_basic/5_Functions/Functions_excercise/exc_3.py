def fizz_buzz(number: int) -> str | int:  # !!!
    """
    Function return:
    "Fizz" - if number is divisible by 3
    "Buzz" - if number is divisible by 5
    "FizzBuzz" - if number is divisible by 3 and 5
    number - otherwise
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


def main():
    input_number = int(input("pls enter number:"))
    print(fizz_buzz(input_number))


if __name__ == "__main__":
    main()
