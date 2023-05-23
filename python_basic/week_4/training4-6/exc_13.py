dictionary = {}
while True:
    print("MENU: ")
    print("1. add word with definition ")
    print("2. find word with definition ")
    print("3. delete word with definition ")
    print("4. END program. ")

    users_choice = input("please chose from 1 to 4: ")
    if users_choice == "1":
        word = input("please enter new word: ")
        definition = input("please enter definition: ")
        dictionary[word] = definition
        print("word and def added")
    elif users_choice == "2":
        word = input("please enter word: ")
        if word in dictionary:
            definition = dictionary[word]
            print(f"definition of word", word, "is: ", definition)
        else:
            print("there is no such word in dictionary")
    elif users_choice == "3":
        word = input("please enter word that u want to delete: ")
        if word in dictionary:
            del dictionary[word]
            print(f"word: ", word, "has been deleted")
        else:
            print(f"word", word, "is not in dictionary")
    elif users_choice == "4":
        print("program finished")
        break
    else:
        print("wrong option choosen. Try again. ")

