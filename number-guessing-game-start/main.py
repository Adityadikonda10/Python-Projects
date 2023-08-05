import random
number = random.randint(1, 100)
print("Welcome to the number guessing game.")
# guess = input("Guess a number between 1 to 100: ")
lives = 0
game_is_on = True
while game_is_on:
    global lives
    guess = input("Guess a number between 1 to 100: ")

    if guess ==
