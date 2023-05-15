import random
players_choice = input("please enter your guess: heads'1' or tails'0': ")
if players_choice != 0 and players_choice != 1:
    print("only chose 0 or 1")
heads = 1
tails = 0

throw = random.randint(0,1)
print(f" 3...2...1...\n {throw}")
