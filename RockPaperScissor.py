import random

def rock_paper_scissors():
    """
    Play a game of Rock, Paper, Scissors against the computer.

    Parameters:
    None

    Returns:
    None

    Example:
    >>> rock_paper_scissors()
    Enter your choice (rock/paper/scissors): rock
    You chose: rock
    Computer chose: scissors
    You win!

    """
    choices = ["rock", "paper", "scissors"]

    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

# Run the game
rock_paper_scissors()