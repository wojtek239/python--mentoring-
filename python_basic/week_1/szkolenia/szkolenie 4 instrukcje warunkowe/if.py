mark = 6
if mark >= 3:
    print("elegancko")

#rozbudowane zadanko tera

mark = int(input("podaj wartość procentowa oceny"))
if mark >= 0 and mark < 20:
# if idzie jak zostaną spełnione warunku
    print("słabiutko, pała")
elif mark >= 20 and mark < 40:
# elif idzie jak nie zostana spełnione warunki
    print("dalej słabo, dwója")
elif mark >=40 and mark < 60:
    print("trója")
elif mark >=60 and mark < 80:
    print("może być, czwóra")
elif mark >=80 and mark < 90:
    print("pjona")
elif mark >=90 and mark <=100:
    print("elegankco, szóstka")
else:
# else idzie na koniec i bez warunku
    print("błędne dane")