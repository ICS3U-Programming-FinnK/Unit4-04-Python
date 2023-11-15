#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: November 15th, 2023
# this program generates a number loop between 0-9 and then it will loop through the numbers
# and it will use the break statement and try catch statement
import random


def main() -> None:
    try:
        # random numbers between 0 to 9
        correct_number = random.randint(0, 9)

        # terminal will loop to keep asking the user to guess the number
        while True:
            try:
                guess = int(input("Guess a number between 0 and 9: "))
                if guess == correct_number:
                    print("Congratulations! You guessed the correct number.")
                    break
                else:
                    print("Try again!")
            # terminal will catch invalid inputs
            except ValueError:
                print("Invalid input. Please enter a number.")

    except ValueError:
        print("Invalid input. Please enter a positive number.")


if __name__ == "__main__":
    main()
