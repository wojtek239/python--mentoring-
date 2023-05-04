n = int(input("podaj ile liczb chcesz wprowadzić: "))
suma = 0
for licznik in range(n):
    liczba = int(input("podaj liczbę nr {}: ".format(licznik)))
    if liczba >= 0:
        suma += liczba
    else:
        print("podałeś zła liczbe. Zeruje i wychodze...")
        suma = 0   #po co to skoro i tak jest break?
        break
print("suma podanych liczb to: ", suma)
print("kunic")

#teraz na continue. Tego trochę nie rozumiem jeszcze...

n = int(input("podaj ile liczb chcesz wprowadzic: "))
suma = 0
for licznik in range (n):
    liczba = int(input("Podaj liczbę nr {}: ".format(licznik)))
    if liczba < 0:
        print("podałeś ujemna liczbę. Ignoruje i nie dodaje do sumy...")
        continue
    suma += liczba
print("suma podanych liczb to: ", suma)
print("koniec")

#o tym temacie chce pogadac na zajeciach
