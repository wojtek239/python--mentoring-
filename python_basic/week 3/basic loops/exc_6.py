print("please enter digits to sum up ")
sum1 = 0
previous_sum = 0

while True:
     digit = int(input("please enter digit: "))
     sum1 += digit

     if sum1 <= previous_sum:
         break
print(f"final sum equals = {sum1}")

