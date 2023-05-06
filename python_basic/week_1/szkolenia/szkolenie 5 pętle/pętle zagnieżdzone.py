# muszą posiadać zmienne i oraz j aby uniknąć nieprawidłowych ilości iteracji pętli
# parametr end= aby nie przechodzić do nowej linii ale wstawić spację

side = int(input("podaj długość boku kwadratu"))
for i in range(side):
    for j in range(side):
        print('*', end='')
print()

#nie rozumiem tego