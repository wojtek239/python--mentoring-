user_number = int(input("please enter number: "))
dividors_sum = 0
def perfect_number(num):
    for i in range(1, num):
        if num % 1 == 0:
            dividors_sum += i
# everytime there is no change while dividing, dividors_sum grows