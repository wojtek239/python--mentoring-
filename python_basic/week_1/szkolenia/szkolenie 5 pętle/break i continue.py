n = int(input("podaj ile liczb chcesz wprowadzić: "))
sum = 0
for numerator in range(n):
    number = int(input("podaj liczbę nr {}: ".format(numerator)))
    if number >= 0:
        sum += number
    else:
        print("podałeś zła liczbe. Zeruje i wychodze...")
        sum = 0
# po co to skoro i tak jest break?
        break
print("suma podanych liczb to: ", sum)
print("kunic")

# teraz na continue. Tego trochę nie rozumiem jeszcze...

n = int(input("podaj ile liczb chcesz wprowadzic: "))
sum = 0
for numerator in range (n):
    number = int(input("Podaj liczbę nr {}: ".format(numerator)))
    if number < 0:
        print("podałeś ujemna liczbę. Ignoruje i nie dodaje do sumy...")
        continue
    sum += number
print("suma podanych liczb to: ", sum)
print("koniec")

#o tym temacie chce pogadac na zajeciach
