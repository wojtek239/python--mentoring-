#muszą posiadać zmienne i oraz j aby uniknąć nieprawidłowych ilości iteracji pętli
#parametr end= aby nie przechodzić do nowej linii ale wstawić spację

bok = int(input("podaj długość boku kwadratu"))
for i in range(bok):
    for j in range(bok):
        print('*', end='')
print()

#nie rozumiem tego