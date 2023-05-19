print("please enter digits to sum up ")
sum1 = 0

while True:
    num = int(input("please enter digit: "))
    sum1 += num

    if num <= 0:
        break
print(f"final sum equals = {sum1}")

sum2 = 0
while num > 0:
    num = int(input("please enter digit: "))
    sum2 += num

print(f"final sum equals = {sum2}")
