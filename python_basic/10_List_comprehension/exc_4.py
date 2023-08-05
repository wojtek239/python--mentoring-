def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))

fib_gen = fibonacci_generator()
for idx, num in enumerate(fib_gen, 1):
    if idx <= 10:
        print(num)

