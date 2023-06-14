with open("test.txt", "r") as f:
    lines = f.readlines()
    fourth_line = lines[3]
    print(fourth_line)
