from Art import logo
import random

number = random.randint(1, 100)


def check(guess, num):
    global gusses
    if guess == num:
        print(f"Guessed number is correct {guess}")
        gusses -= gusses
        return gusses

    elif guess > num:
        print(f"{guess} is too high")
        gusses -= 1
        return gusses
    else:
        print(f"{guess} is too low")
        gusses -= 1
        return gusses



print(logo)

print("Welcome to the Number Guessing Game")
print("I am thinking of a number from 1-100")
# guess_number = int(input("Guess the number between 1 and 100\n"))
difficulty = input("Enter 'easy' or 'hard'\n").lower()
print(f"Pssst number is {number}")

# GAME_RUNNING = False
# while GAME_RUNNING:

if difficulty == "easy":
    gusses = 10
    while gusses > 0:
        guess_number = int(input("Guess the number between 1 and 100\n"))
        check(guess_number, number)

        print(f"You have {gusses} left.")

else:
    gusses = 5
    while gusses > 0:
        guess_number = int(input("Guess the number between 1 and 100\n"))
        check(guess_number, number)
        # gusses -= 1
        print(f"You have {gusses} left.")



