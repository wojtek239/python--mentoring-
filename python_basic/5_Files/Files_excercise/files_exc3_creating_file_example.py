with open("example.txt", "w") as file:
    file.write("Litwo, Ojczyzno moja! ty jesteś jak zdrowie;\n")
    file.write("Ile cię trzeba cenić, ten tylko się dowie,\n")
    file.write("Kto cię stracił. Dziś piękność twą w całej ozdobie\n")


with open("example.txt", "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines, start=1):
        if i % 2 == 0:
            print(line.strip())
