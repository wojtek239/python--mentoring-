"""
content of pasta.txt file
i love italian pasta
especially spaghetti
"""

with open("pasta.txt", encoding="utf-8") as file:
    print(file.readline())
    print(file.tell())
    print(file.readline())

    file.seek(28)
    file.readline()