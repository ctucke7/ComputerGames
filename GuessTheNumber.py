import math
import random

#GameWelcome
print("Welcome to 'Can You Guess It!'" )
print("The rules of the game are simple.\nYou will create a range and then try to guess\nthe randomly selected number by the program\nin the least amount of guesses as possible!")
low = int(input("Select your min: "))
high = int(input("Select your max: "))

#RequiredInput
while low >= high:
    low = int(input("Invalid input, make sure min is smaller than max! "))
print(f"Your range is between {low} and {high}.")

#Variables
maxm = math.ceil(math.log2(high - low + 1))
user = int(input(f"You have {maxm} guesses including this one so choose wisely! What will your first guess be? "))
rand = int(random.uniform(low, high))
guess = 1

#GamePlay
if user == rand:
    print(f"Congrats! You got it in the least amount of guesses!")
else:
    while user != rand:
        if guess == maxm:
            print(f"Ran out of guesses, the answer was {rand}. Better luck next time!")
            break
        else:
            while guess != maxm:
                if user > rand:
                    guess += 1
                    print("Nope! Think smaller!")
                    user = int(input("Try again: "))
                    if user == rand:
                        print("Congrats! You got it!")
                        break
                elif user < rand:
                    guess += 1
                    print("Not Quite! Think bigger!")
                    user = int(input("Try again: "))
                    if user == rand:
                        print(f"Congrats! You got it in {guess} guesses!")
                        break




