ocena = 6
if ocena >= 3:
    print("elegancko")

#rozbudowane zadanko tera

ocena = int(input("podaj wartość procentowa oceny"))
if ocena >= 0 and ocena < 20:             #if idzie jak zostaną spełnione warunku
    print("słabiutko, pała")
elif ocena >= 20 and ocena < 40:          #elif idzie jak nie zostana spełnione warunki
    print("dalej słabo, dwója")
elif ocena >=40 and ocena < 60:
    print("trója")
elif ocena >=60 and ocena < 80:
    print("może być, czwóra")
elif ocena >=80 and ocena < 90:
    print("pjona")
elif ocena >=90 and ocena <=100:
    print("elegankco, szóstka")
else:                                      #else idzie na koniec i bez warunku
    print("błędne dane")