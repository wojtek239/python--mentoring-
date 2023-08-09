def my_generator():
    values = [1, 2, 3, 4, 5]
    for val in values:
        yield val


gen = my_generator()
print(next(gen))  
print(next(gen))

gen = my_generator()
print(gen.__next__())
print(gen.__next__())

gen = my_generator()
for _ in range(3):
    print(next(gen))

try:
    for _ in range(10):
        print(next(gen))
except StopIteration:
    print("Iteration,got example")

print("Nope, try-except")

gen = my_generator()
for num in gen:
    print(num)
