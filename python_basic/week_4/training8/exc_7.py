user_number = int(input("pls enter n number for Fibonacci sequence: "))


def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence


fibonacci_sequence = fibonacci(user_number)
print(fibonacci_sequence)
