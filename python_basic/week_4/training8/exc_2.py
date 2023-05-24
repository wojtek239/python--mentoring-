users_word = input("please enter ur word: ")
print(users_word)
reversed_word = users_word[::-1]
print(reversed_word)

if users_word == reversed_word:
    print("this is palindrome")
else:
    print("this is not a palindrome")