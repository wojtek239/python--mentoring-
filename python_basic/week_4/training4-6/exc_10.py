import random
opening_val = int(input("please enter opening value: "))
closing_val = int(input("please enter closing value: "))
# range a nie value   przy bool ma byc is
guessed_number = random.randint(opening_val, closing_val)
score = closing_val - opening_val

while True:
    users_guess = int(input("please take your guess: "))
    if users_guess == guessed_number:
        print(f'bravo ! {users_guess} is a good guess')
        print(f"You have {score}, points")
        break

    elif users_guess < guessed_number:
        score -= 1
        print("your guess is too low, please try again: ")

    elif users_guess > guessed_number:
        score -= 1
        print("your guess is too high, please try again: ")

    if score <= 0:
        print("lol u lost")
        break

