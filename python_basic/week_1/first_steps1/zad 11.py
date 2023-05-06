name_1 = "Wojtek"
name_2 = "Alan"
a = (name_1[0:3])
b = (name_2[-2:])
# dzięki temu od drugiej litery od tylu do konca napisu poszło wyciecie
# nic innego nie działało
print(a)
print(b)

name_3 = a + b
print(name_3)
