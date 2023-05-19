input1 = input("player1 enter rock/paper/scissors: ")
input2 = input("player2 enter rock/paper/scissors: ")
if input1 == "rock" and input2 == "paper":
    print("player2 wins")
elif input1 == "rock" and input2 == "scissors":
    print("player1 wins")
elif input1 == input2:
    print("draw")
elif input1 == "paper" and input2 == "scissors":
    print("player2 wins")
elif input1 == "paper" and input2 == "rock":
    print("player1 wins")
elif input1 == "scissors" and input2 == "rock":
    print("player2 wins")
elif input1 == "scissors" and input2 == "paper":
    print("player1 wins")
else:
    print("wrong data")

choices = ['rock', 'paper', 'scissors']

if input1 and input2 in choices:
    if input1 == input2:
        print('draw')
    elif (input1 == "paper" and input2 == 'rock') or () or ():
        print("WIN player 1")
    else:
        print("WIN player 2")
else:
    print('wrong data')
