

# Number guessing Game!
import random
import sys
import time
from colorama import Fore


def headlines(text):
    for sentence in text:
        sys.stdout.write(sentence)
        sys.stdout.flush()
        time.sleep(0.05)


headlines(Fore.CYAN + "Welcome to the Number guessing Game!""\n")
headlines(Fore.CYAN + "I'm thinking of a number between 1 and 100.""\n")
headlines(Fore.CYAN + "You have 5, 10, 15 chance to guess the correct number.""\n")


def menu():
    print(Fore.YELLOW+"Please Select the difficulty level:")
    print(Fore.YELLOW+"1. Easy (15 chances)")
    print(Fore.YELLOW+"2. Medium (10 chances)")
    print(Fore.YELLOW+"3. Hard (5 chances)")
    print(Fore.YELLOW + "0. Hand over")
    choose = int(input("Enter your choice: "))

    return choose


def easy():
    chances = 15
    number = random.randint(1, 100)
    print("Fine! You have selected the Easy difficulty level.")
    while chances > 0:
        guess = int(input("Enter your guess (1-100): "))
        if guess > number:
            print(f"Incorrect! The number is less than {guess}.")
            chances -= 1
        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}.")
            chances -= 1
        elif guess == number:
            print("Correct!")
            break
    print(f"Chances left: {chances}")
    if chances == 0:
        print(Fore.RED + f"YOu lost the number was {number}.")
    return guess


def Medium():
    chances = 10
    number = random.randint(1, 100)
    print("Boldness! You have selected the Medium difficulty level.")
    while chances > 0:
        guess = int(input("Enter your guess (1-100): "))
        if guess > number:
            print(f"Incorrect! The number is less than {guess}.")
            chances -= 1
        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}.")
            chances -= 1
        elif guess == number:
            print("Correct")
            break
    if chances > 0:
        print(Fore.GREEN + f"Congratulations! You guessed the correct number.")
    if chances == 0:
        print(Fore.RED + f"You lost the number was {number}.")

    return guess


def Hard():
    chances = 5
    number = random.randint(1, 100)
    print("AMAZING! You have selected the hard difficulty level.")
    while chances > 0:
        guess = int(input("Enter your guess: "))
        if guess > number:
            print(f"Incorrect! The number is less than {guess}.")
            chances -= 1
        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}.")
            chances -= 1
        elif guess == number:
            print("Correct")
            break
    if chances > 0:
        print(Fore.GREEN + f"Congratulations! You guessed the correct number.")
    if chances == 0:
        print(Fore.RED + f"You lost the number was {number}.")
    return None


def main():
    while True:
        choice = menu()
        if choice == 1:
            easy()
        elif choice == 2:
            Medium()
        elif choice == 3:
            Hard()
        elif choice == 0:
            print(Fore.RED + "Hand over!")
            break
        else:
            print("Selection is not avaible, Try again!")

    print("It's great that you wasted your time on me")
    print("See you next time.")
    return


if __name__ == "__main__":
    main()
