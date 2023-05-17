k = int(input("please enter k: "))
for i in range (50, 101):
    if (2 ** i) % k == 0:
    print(2 ** i)