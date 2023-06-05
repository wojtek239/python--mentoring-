lines = ["Ala has a cat\n", "i like it\n"]

with open("example.txt", "w") as file:
    file.writelines(lines)

file.writelines(lines)
