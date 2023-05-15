amount_of_cats = int(input("How many cats does Ala have? ")) + 3

sentence = f"Ala found 3 more cats todday. She now has {amount_of_cats} cats."
print(sentence)

print(sentence.split(' '))
print(sentence.replace(" ", "\n"))

if sentence.islower():
    print("every letter is small :) ")
else:
    print("not every letter is small :( ")

smol_sentence = sentence.lower()
print(smol_sentence)