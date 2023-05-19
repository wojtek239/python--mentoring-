import random
players_choice = input("please enter your guess: heads'0' or tails'1': ")
while players_choice != "0" and players_choice != "1":
    print("only chose heads or tails")
    break
throw = random.randint(0, 1)
print(f" 3...2...1...\n {throw}")
if "0":
    print("heads")
if "1":
    print("tails")
if players_choice == throw:
    print("player scores a point")
if players_choice != throw:
    print("computer scores a point")

