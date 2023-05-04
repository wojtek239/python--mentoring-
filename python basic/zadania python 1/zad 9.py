napis = input("Proszę podać napis: ")
if len(napis) < 2:      #sprawdzic dlugosc napisu
    print("napis jest za krótki")
else:
    pierwsza_litera = napis[0]   #zabrac pierwsza i ostatnia litere
    ostatnia_litera = napis[-1]
    nowy_napis = ostatnia_litera + napis[1:len(napis)-1] + pierwsza_litera   #suma ostatniej litery, napisu bez pierwszej i ost litery i pierwszej litery
print("nowy napis to: ", nowy_napis)