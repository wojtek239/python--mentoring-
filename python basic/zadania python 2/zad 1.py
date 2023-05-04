napis = input("proszę podać stringa (min 7 znaków): ")
if len(napis) <= 6:
    print("napis za krótki")
else:
    print("string brzmi: ", napis)
    print("string zawiera ",len(napis), "znaków" )
    print("pierwszy i ostatni znak stringa to: ", napis[0], "oraz",  napis[-1])
    print(napis[len(napis) - 3])
    print(napis[len(napis) - 2])
    print(napis[len(napis) - 4])
    print("trzy znaki ze środka stringa to niestety nie wiem jak zrobić, nie umiem randomizacji") #random? random.uniform?