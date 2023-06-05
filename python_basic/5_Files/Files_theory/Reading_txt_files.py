file = open("example.txt", "r")
sign = file.read(1)
print(f"first sign is: ", sign)

sign = file.read(1)
# nie powinno byc 2 tutaj?

print("other signs: ")
while sign:
    print(sign)
    sign = file.read(1)

file.close()