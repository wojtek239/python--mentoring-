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
print("3...2...1... throw ! ")
while computer_choice == 0:
    print("computer choose eagle.")
    break
while computer_choice == 1:
    print("computer choose tails.")
    break
while players_choice == "0" and computer_choice == "0":
        print("draw")
        break


