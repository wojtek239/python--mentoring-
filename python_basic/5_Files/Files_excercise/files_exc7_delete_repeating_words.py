with open("example.txt", "r") as f:
    content = f.read()

no_repeat = " ".join(set(content.split()))

with open("example_without_repeat.txt", "w") as f:
    f.write(no_repeat)
