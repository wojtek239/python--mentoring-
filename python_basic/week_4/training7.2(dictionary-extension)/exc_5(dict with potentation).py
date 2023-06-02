n = int(input("please enter n: "))
dictionary = {
    x: x*x
    for x in range(1, n+1)
}
print(dictionary)
