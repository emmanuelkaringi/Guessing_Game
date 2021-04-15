#Import random module

import random

#Assign it to a variable

num = random.randint(1,100)

#Introduce player to the game
print("WELCOME TO GUESS IT!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're BAD")
print("If your guess is within 10 of my number, I'll tell you you're GOOD")
print("If your guess is farther than your most recent guess, I'll say you're becomming BADDER")
print("If your guess is closer than your most recent guess, I'll say you're getting CLOSE")
print("ENJOY!")

#Create a list to store Guesses
guesses = [0]

#Ask for a guess and test it
while True:
    guess = int(input("I'm thinking of a number between 1 and 100. What is your guess? \n"))
    if guess < 1 or guess > 100:
        print("Wrong guess, Please try again: ")
        continue
    break

#Compare the player's guess to your number range
while True:
    guess = int(input("I'm thinking of a number between 1 and 100. What is your guess? \n"))
    if guess < 1 or guess > 100:
        print("Wrong guess, Please try again: ")
        continue
    if guess == num:
        print(f"CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!")
        break
    guesses.append(guess)

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print("BADDER")
        else:
            print("Almost There!!")
    else:
        if abs(num-guess) <= 10:
            print("GOOD")
        else:
            print("BAD")