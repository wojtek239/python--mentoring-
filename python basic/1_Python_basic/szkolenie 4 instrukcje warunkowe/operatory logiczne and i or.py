#koniunkcja dwuargumentowa to np 'and'. Łączymy dwa warunki i oba musza byc spełnione
#alternatywa logiczna to 'or'. Przynajmniej jedenz warunków musi byc spełniony

print(bool(1))
print(bool(0))

#bool traktuje każda inna niz 0 liczbe jako true. tak samo każdy niepusty str

print(bool(18181818))
print(bool(-1010101))

#not (zaprzeczanie/ odwrotność)  można łączyć bezpośrednio z true albo false
print(not True)
print(not(bool("abcd")))