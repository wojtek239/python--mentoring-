file = open("D:/file.txt", "w")
file.write("learn programming with devs-mentoring")
file.close()




file = open("example.txt", "w")
lines = ['Ala has a cat\n', 'this cat is cool\n']
file.writelines(lines)
file.close()
