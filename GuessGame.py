import random

def guess_the_number():
    """
    A number guessing game where the user has to guess a secret number between 1 and 100.

    The game continues until the user guesses the correct number. The number of attempts is tracked and displayed at the end.

    Example:
        >>> guess_the_number()
        Welcome to the Number Guessing Game!
        I'm thinking of a number between 1 and 100.
        Your guess: 50
        Too low! Try again.
        Your guess: 75
        Too high! Try again.
        Your guess: 67
        Congratulations! You guessed the number in 3 attempts.

    Returns:
        None
    """
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Run the game
guess_the_number()