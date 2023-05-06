inscription = input("proszę podać stringa (min 7 znaków): ")
if len(inscription) <= 6:
    print("napis za krótki")
else:
    print("string brzmi: ", inscription)
    print("string zawiera ",len(inscription), "znaków" )
    print("pierwszy i ostatni znak stringa to: ", inscription[0], "oraz",  inscription[-1])
    print(inscription[len(inscription) - 3])
    print(inscription[len(inscription) - 2])
    print(inscription[len(inscription) - 4])
    print("trzy znaki ze środka stringa to niestety nie wiem jak zrobić, nie umiem randomizacji")
# random? random.uniform?