with open("example.txt", "r") as file:
    content = file.read()

no_repeat = " ".join(set(content.split()))

with open("example_without_repeat.txt", "w") as new_file:
    new_file.write(no_repeat)