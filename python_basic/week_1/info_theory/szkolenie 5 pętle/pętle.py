# pętla while
ammount = int(input("podaj ile razy chcesz wyświetlić napis: "))
numerator = 0
while numerator < ammount:
# skąd licznik wie że się ma zwiększać o 1. Jak to += 1 działa?
    print("poznaj pętle")
    numerator += 1
# gdyby tego nie było to by proces ciągle sie powtarzał bez konca
# pętla for
ammount2 = int(input("podaj ile razy chcesz wyświetlić napis: "))
for numerator in range(ammount2):
# in range automatycznie zaczyna liczyc od 0 chyba ze napiszemy inaczej
    print("poznaj pętle")

# zeby liczyć od końca trzeba dodać trzeci argument dla range (-1)
print("do wybuchu zostalo: ")
for i in range(10, 0, -2):
# i to zmienna iteracyjna/zaleznosci od wartosci argumentu dla range jak bd -2 to bedzie odliczac co dwa
    print(str(i) + "...")
# czemu str?
print("buum ! ")