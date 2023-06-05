file = open("example.txt", "r")
sign = file.read(1)
print(f"first sign is: ", sign)

sign = file.read(1)


print("other signs: ")
while sign:
    print(sign)
    sign = file.read(1)

file.close()

# file = open("example.txt", "r")
# first_line = file.readline()
# second_line = file.readline()

# file.close()