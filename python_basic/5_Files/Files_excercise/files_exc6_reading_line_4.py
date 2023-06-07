with open("test.txt", "r") as file:
    lines = file.readlines()
    fourth_line = lines[3]
    print(fourth_line)