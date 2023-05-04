string1 = "Wojtek123"
string2 = "Wojtek 123"
print(string1.isalnum())
print(string2.isalnum()) #spacja nie jest alfanumeryczna
string3 = "123"
string4 = "Wojtek lubi banany"
print(string3.isdigit())
print(string4.isdigit()) #nie ma samych cyfr tu
string5 = "abecadło"
string6 = "123456abc"
print(string5.isalpha())
print(string6.isalpha()) #tu nie ma samych liter
string7 = "       "
string8 = "chyba to ogarniam"
print(string7.isspace())
print(string8.isspace()) #tu nie ma samych białych znaków
string9 = "mała litera"
string10 = "Duża litera"
print(string9.islower())
print(string10.islower()) #tu nie ma samych małych liter
string11 = "DUŻE LITERY"
string12 = "małe litery"
print(string11.isupper())
print(string12.isupper()) #tu nie ma samych dużych liter
string13 = "Przykład Tytułu"
string14 = "niewiadomo co"
print(string13.istitle())
print(string14.istitle()) #tu nie ma pierwszych dużych liter