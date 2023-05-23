colours_list = ["green", "red", "blue", "black", "purple", "navy blue", "blue", "black", "black", "green",
                "lime", "navy blue", "blue", "indigo", "green", "red"]

amount_of_elements = len(colours_list)

colours_set = set(colours_list)
print(colours_set)

amount_of_colours = len(colours_set)
print(amount_of_colours)

print("elements: ")
for colour in colours_set:
    print(colour)

colours_set.add("orange")
print(f"after adding set is: ", colours_set)

colours_set.remove("purple")
print(f'after deleting set is: ', colours_set)
