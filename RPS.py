'''
Task 2 : Rock, paper, scissors game
Create a program that allows the user to play
the classic game of rock, paper, scissors
against the computer.

'''
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "---------->You win!<----------"
    else:
        return "---------->Computer wins!<----------"

def main():
    print("Welcome to Rock, Paper, Scissors!")

    choices = ['rock', 'paper', 'scissors']

    while True:
        player_choice = input("Enter your choice (rock/paper/scissors) or 'quit' to exit: ").lower()

        if player_choice == 'quit':
            print("Thanks for playing!")
            break

        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)

        print(f"You chose {player_choice}")
        print(f"Computer chose {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "---------->It's a tie!<----------"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "---------->You win!<----------"
    else:
        return "---------->Computer wins!<----------"

def main():
    print("Welcome to Rock, Paper, Scissors!")

    choices = ['rock', 'paper', 'scissors']

    while True:
        player_choice = input("Enter your choice (rock/paper/scissors) or 'quit' to exit: ").lower()

        if player_choice == 'quit':
            print("Thanks for playing!")
            break

        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)

        print(f"You chose {player_choice}")
        print(f"Computer chose {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()

