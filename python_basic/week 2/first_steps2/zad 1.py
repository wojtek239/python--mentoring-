import random

inscription = input("proszę podać stringa (min 7 znaków): ")

if len(inscription) <= 6:
    print("napis za krótki")
else:
    print("string brzmi: ", inscription)
    print("string zawiera ", len(inscription), "znaków" )

    print("pierwszy i ostatni znak stringa to: ", inscription[0], "oraz",  inscription[-1])

    print(inscription[random.randint(0, len(inscription) - 1)])
    print(inscription[random.randint(0, len(inscription) - 1)])
    print(inscription[random.randint(0, len(inscription) - 1)])


# random? random.uniform
