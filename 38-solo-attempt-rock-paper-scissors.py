# 38 (03:10:26) rock, paper, scissors game 🗿
import random

choices = ['rock', 'paper', 'scissors']

def print_win_msg():
    print("You win!")

def print_lose_msg():
    print("You lose, better luck next time")

while (True):
    computer = random.choice(choices)
    player = None

    def print_choices():
        print("Player:", player)
        print("Computer:", computer)

    # Ensure user input is valid
    while (player not in choices):
        if player != None: print("Invalid choice, try again...")
        player = input("rock, paper or scissors?: ")

    # Win / lose / draw conditions
    print_choices()

    if computer == player:
        print("Draw")
    elif computer == "rock":
        # Win
        if player == "paper":
            print_win_msg()
        # Lose
        elif player == "scissors":
            print_lose_msg()
    elif computer == "paper":
        # Win
        if player == "scissors":
            print_win_msg()
        # Lose
        elif player == "rock":
            print_lose_msg()
    elif computer == "scissors":
        # Win
        if player == "rock":
            print_win_msg()
        # Lose
        elif player == "paper":
            print_lose_msg()

    # Ask to play again
    play_again = input("Would you like to play again (y/n)? ")
    while play_again not in ('y', 'n'):

        play_again = input("Would you like to play again (y/n)? ")

    # Exit game loop conditions
    if play_again == 'n':
        break

    print() # new game, new line


print("\nThanks for playing!")
