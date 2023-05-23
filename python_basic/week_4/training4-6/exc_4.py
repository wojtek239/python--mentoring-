day_number = int(input("please enter number from 1 to 7: "))
while day_number not in range(1, 8):
    print("there is no such day")
    break
if day_number == 1:
    print("it's Monday")
elif day_number == 2:
    print("it's Tuesday")
elif day_number == 3:
    print("it's Wednesday")
elif day_number == 4:
    print("it's Thursday")
elif day_number == 5:
    print("it's Friday")
elif day_number == 6:
    print("it's Saturday")
elif day_number == 7:
    print("it's Sunday :( ")
