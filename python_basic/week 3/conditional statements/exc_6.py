import random
players_score = 0
computer_score = 0

players_choice = input("please enter '0' for eagle and '1' for tails: ")

while players_choice == "0":
    print("you choose eagle.")
    break
while players_choice == "1":
    print("you choose tails.")
    break
#while players_choice != "0" or players_score != "1":
#    print("only choose 0 or 1.")
#    break
computer_choice = random.randint(0, 1)

while computer_choice == 0:
    print("computer choose eagle.")
    break
while computer_choice == 1:
    print("computer choose tails.")
    break
while players_choice == "0" and computer_choice == "0":
        print("draw")
        break
print("3...2...1... throw ! ")
throw = random.randint(0, 1)
print(f'{throw} was thrown, which means: ')
if throw == 0:
    print("eagle")
if throw == 1:
    print("tails")
while players_choice == 0 and throw == 0:
    print("player scores a point !")
    break
while computer_choice == 1 and throw == 1:
    print("computer scores a point !")
    break