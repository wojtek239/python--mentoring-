my_fav_colours = {"green", "purple", "red", "gold"}
user_fav_colours = input("please enter ur fav colours: ")
user_colours = set(user_fav_colours.split())

print(user_colours)
if my_fav_colours == user_colours:
    print("both sets are the same")
else:
    print("they are not the same")

doubled_colours = my_fav_colours.intersection(user_colours)
print(f"doubled colours are: ", doubled_colours)

print(f"my fav colours are: ", my_fav_colours)
print(f"your fav colours are: ", user_colours)