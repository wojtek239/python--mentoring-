class InvalidNumberError(Exception):
    pass


class DivisionByZeroError(Exception):
    pass


class Example3Error(Exception):
    pass


def example1():
    for i in range(3):
        try:
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
            if y == 0:
                raise DivisionByZeroError("U can't divide by 0")
            print(x, '/', y, '=', x/y)
        except ValueError:
            print("Error: enter correct number")
        except DivisionByZeroError as e:
            print(f"Error: {e}")


def example2(L):
    print("\n\nExample 2")
    sumOfPairs = []
    try:
        for i in range(len(L) - 1):
            sumOfPairs.append(L[i] + L[i + 1])
    except IndexError:
        print("Error: List has not enough elements")
    else:
        print("sumOfPairs =", sumOfPairs)


def example3(L):
    try:
        if len(L) < 4:
            raise Example3Error("List must contain at least 4 elements")
    except Example3Error as e:
        print(f"Error: {e}")


def printUpperFile(fileName):
    try:
        with open(fileName, "r") as file:
            for line in file:
                print(line.upper())
    except FileNotFoundError:
        print(f"Error: File '{fileName}' does not exist.")
    except Exception as e:
        print(f"Error: Unexpected exception: {e}")


def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])
    example3([10, 3, 5, 6])

    printUpperFile("doesNotExistYet.txt")
    printUpperFile("./Desktop/misspelled.txt")


if __name__ == "__main__":
    main()
