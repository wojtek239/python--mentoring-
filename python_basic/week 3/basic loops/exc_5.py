k = int(input("please enter k: "))
for i in range (50, 101):
    if i % k == 0:
        print(i)

u = int(input("please enter opening interval: "))
u2 = int(input("please enter closing interval: "))
for i in range (u, u2):
    if i % (k) == 0:
        print(i)