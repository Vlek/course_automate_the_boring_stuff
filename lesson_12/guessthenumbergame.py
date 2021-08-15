"""
Guess the number game.

This is a culmination of the things talked about in the
previous lessons to create a complete game.

The game asks for the user's name and then gives the
player a few tries to guess a number with win/lose conditions.

We do not have classes yet, so I will be doing this using
just functions. I am going to change this a bit to use
a main function to better handle scopped variables such
as the player's name.
"""

from random import randint


RANDOM_NUM_LOWER_LIMIT: int = 1
RANDOM_NUM_UPPER_LIMIT: int = 20
GUESSES_ALLOWED: int = 7
GREETING: str = "Hello, what is your name?: "


def main() -> None:
    """The main runner for the guess the number game."""

    playerName = input(GREETING)

    randomNumber: str = str(randint(
            RANDOM_NUM_LOWER_LIMIT,
            RANDOM_NUM_UPPER_LIMIT + 1))

    guess: str = ''

    for guess_chance in range(1, GUESSES_ALLOWED + 1):

        guess: str = input(f"Guess #{guess_chance}: ")

        if guess < randomNumber:
            print("Your guess is too low")
        elif guess > randomNumber:
            print("Your ugess is too high")
        else:
            break

    if guess == randomNumber:
        print(f"Great job, {playerName}! "
              f"You guessed the right number: {randomNumber}")
    else:
        print(f"Tough luck, {playerName}. "
              f"The number I was thinking of was {randomNumber}")


if __name__ == "__main__":
    main()
