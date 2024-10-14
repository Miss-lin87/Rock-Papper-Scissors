from random import randint as ran

# This converts the computers random pick of 1 - 3 into a string.
def convert(computer):
    if computer == 1:
        computer = "Rock"
        return computer
    elif computer == 2:
        computer = "Papper"
        return computer
    else:
        computer = "Scissors"
        return computer
# This checks the players pick towards the computers pick. Will display one of tre outcomes, Win, Lose or Draw
def check(x, y):
    if x == y:
        print("The round is a Draw")
    elif (x == "Rock" and y == "Scissors") or (x == "Scissors" and y == "Papper") or (x == "Papper" and y == "Rock"):
        print("you win this round")
    else:
        print ("You lose this round")

# The module for actuallt calling and runing a game
def game():
    player = str.capitalize(input("Pick Rock, Papper or Scissors ")) # players input returned with capital letter
    if player == "Rock" or "Papper" or "Scissors": # run game if the input is valid
        print("You picked: " + str(player))
        computer = convert(int(ran(1, 3)))
        print("The computer picked: " + str(computer))
        check(player, computer)
    else:
        print("invalid input, try again") # if none valid input is made then return invalid inut and run again
        game()

game()