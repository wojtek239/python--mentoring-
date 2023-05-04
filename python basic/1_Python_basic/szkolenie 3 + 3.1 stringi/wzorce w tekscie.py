string = "Devs-Mentoring to super sprawa"
position1 = string.find("to")
position2 = string.find("ej")
print(position1)
print(position2) # find daje -1 gdy nie ma

string2 = "Devs-Mentoring to super sprawa jest"
position3 = string2.index("to")
print(position3)
position4 = string2.index("ej") #index daje error gdy nie ma
print(position4)
