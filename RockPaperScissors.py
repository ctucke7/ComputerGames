import random
import time


options = ("rock", "paper", "scissors")

option = random.choice(options)
play = ""

#select = input("Choose: rock, paper, or scissors! ").lower()

#for x in options:
    #print(x)
    #time.sleep(1)

while not play == "q":
    select = input("Choose: rock, paper, or scissors! ").lower()
    if select not in options:
        while select not in options:
            select = input("Invalid choice! Choose: rock, paper, or scissors! ").lower()
    for x in options:
        print(x)
        time.sleep(1)
    if select in options:
        if select == option:
            print(f"{select} ties {option}")
            option = random.choice(options)
            play = input("Press 'enter' to play again and 'q' to quit. ").lower()
            if "q" in play:
                break
        elif select == "paper" and option == "rock":
            print(f"{select} beats {option}")
            print("YOU WIN!")
            option = random.choice(options)
            play = input("Press 'enter' to play again and 'q' to quit. ").lower()
            if "q" in play:
                break
        elif select == "rock" and option == "scissors":
            print(f"{select} beats {option}")
            print("YOU WIN!")
            option = random.choice(options)
            play = input("Press 'enter' to play again and 'q' to quit.").lower()
            if "q" in play:
                break
        elif select == "scissors" and option == "paper":
            print(f"{select} beats {option}")
            print("YOU WIN!")
            option = random.choice(options)
            play = input("Press 'enter' to play again and 'q' to quit.").lower()
            if "q" in play:
                break
        else:
            print(f"{option} beats {select}. YOU LOSE!")
            play = input("Press 'enter' to play again and 'q' to quit. ").lower()
            option = random.choice(options)
            if "q" in play:
                break
    else:
        print("Invalid choice!")
#number = random.randint(1,6) random number within the range assigned
#number = random.random() random floating point number

