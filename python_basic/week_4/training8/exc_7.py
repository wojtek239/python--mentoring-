n = int(input("pls enter n number for Fibonachi sequence: "))


def fibonachi(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence


fibonachi_sequence = fibonachi(n)
print(fibonachi_sequence)
