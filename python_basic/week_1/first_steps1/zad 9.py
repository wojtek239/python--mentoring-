inscription = input("Proszę podać napis: ")

# sprawdzic dlugosc napisu
if len(inscription) < 2:
    print("napis jest za krótki")
else:
    # zabrac pierwsza i ostatnia litere
    # pierwsza_litera = napis[0]
    # ostatnia_litera = napis[-1]

    # suma ostatniej litery, napisu bez pierwszej i ost litery i pierwszej litery
    # nowy_napis = ostatnia_litera + napis[1:len(napis) - 1] + pierwsza_litera
    new_inscription = inscription[-1] + inscription[1:len(inscription) - 1] + inscription[0]
print("nowy napis to: ", new_inscription)
