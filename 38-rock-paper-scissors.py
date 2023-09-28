# 38 (03:10:26) rock, paper, scissors game 🗿
import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)

    # Initialise player with None
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    # Print fns
    def print_choices():
        print("player:", player)
        print("computer:", computer)

    def print_loser_msg():
        print("You lose :( better luck next time")

    def print_draw_msg():
        print(f"Draw, you both chose {player}")

    def print_winner_msg():
        print("Woohooo! You win!")

    print_choices()

    # Win conditions
    # Draw
    if player == computer:
        print_draw_msg()
    elif player == "rock":
        # Loss
        if computer == "paper":
            print_loser_msg()
        # Win
        elif computer == "scissors":
            print_winner_msg()
    elif player == "paper":
        # Loss
        if computer == "scissors":
            print_loser_msg()
        # Win
        elif computer == "rock":
            print_winner_msg()
    elif player == "scissors":
        # Loss
        if computer == "rock":
            print_loser_msg()
        # Win
        elif computer == "paper":
            print_winner_msg()
    else:
        print("Well this is kinda awkward, I didn't expect you to be here :S")

    # Ask user to play again or not
    # Define valid user input response
    yes_play_again = ["yes", "y"]
    no_play_again = ["no", "n"]
    play_again_choices = yes_play_again + no_play_again

    play_again = input("Would you like to play again?: ")

    # If user input is not valid, ask again until valid input received
    while play_again not in play_again_choices:
        print("Please enter either yes/no or y/n.")
        play_again = input("Would you like to play again?: ")

    # If user says yes/y, continue game loop
    # If user says no/n, break out of game loop
    if play_again in ["no", "n"]:
        break

    print()  # new line to separate game logs

print("Thanks for playing, bye!")
