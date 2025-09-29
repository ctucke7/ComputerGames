import random

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = []
comp = []
user = []

x = 0

for i in cards:
    x = 0
    while x < 4:
        deck.append(i)
        x += 1

running = True
print("Welcome to the game of 21!")
print("The rules are simple. You want to get as close to 21 as possible without going over!")
print("Once you are done drawing, type 'n' to stop.")
print("If the dealer gets closer to 21 than you, YOU LOSE!")
print()

while running:
    done = input("Would you like to play?(Q to quit, ENTER to play)")
    if done == "Q" or done == "q": break

    if len(deck) < 10:
        deck = []
        for i in cards:
            x = 0
            while x < 4:
                deck.append(i)
                x += 1

    #computer dealer gets cards
    comp_pick1 = random.choice(deck)
    deck.remove(comp_pick1)
    comp.append(comp_pick1)
    comp_pick2 = random.choice(deck)
    deck.remove(comp_pick2)
    comp.append(comp_pick2)
    print(f"The dealer has a {comp[0]}")

    #user gets cards
    user_pick1 = random.choice(deck)
    deck.remove(user_pick1)
    user_pick2 = random.choice(deck)
    deck.remove(user_pick2)
    user.append(user_pick1)
    user.append(user_pick2)
    print(f"Your hand: {user}")

    #user hit game play
    game_running = True

    user_total = 0
    comp_total = 0

    for i in user:
        if i.isalpha() and i != 'A':
            user_total += 10
        elif i == 'A':
            ace = int(input("Do you want you Ace to be 1 or 11? "))
            print()
            user_total += ace
        else:
            user_total += int(i)

    for i in comp:
        if i.isalpha() and i != 'A':
            comp_total += 10
        elif i == 'A':
            comp_total += 1
        else:
            comp_total += int(i)

    while game_running:

        if user_total == 21:
            hit = 'n'
        else:
            hit = input("Do you want to hit?(y/n) ")
            print()

        while hit == "y":
            user_hit = random.choice(deck)
            user.append(user_hit)
            if user_hit.isalpha() and user_hit != 'A':
                user_total += 10
            elif user_hit == 'A':
                print(user)
                ace = int(input("Do you want your Ace to be 1 or 11? "))
                print()
                user_total += ace
            else:
                user_total += int(user_hit)

            if user_total == 21:
                break
            if user_total > 21:
                if 'A' not in user:
                    break
                elif 'A' in user and ace == 1:
                    break
                elif 'A' in user and ace != 1:
                    user_total -= 10
            if user_total < 21:
                print(f"The dealer has a {comp[0]}")
                print(f"Your hand: {user}")
                hit = input("Do you want to hit?(y/n) ")
                print()

        if user_total > 21:
            print(f"Dealer: {comp}, User:{user}")
            print(f"Dealer: {comp_total}, User:{user_total}")
            print()
            print("Oops you bust!")
            print()
            user = []
            comp = []
            break

        while comp_total < 17:
                comp_hit = random.choice(deck)
                comp.append(comp_hit)
                if comp_hit.isalpha() and comp_hit != 'A':
                    comp_total += 10
                elif comp_hit == 'A':
                    comp_total += 1
                else:
                    comp_total += int(comp_hit)

        #Results
        print(f"Dealer: {comp}, User:{user}")
        print(f"Dealer: {comp_total}, User:{user_total}")
        print()

        if comp_total > 21:
            print("You win!")
            print()
        elif user_total > comp_total:
            print("You win!")
            print()
        elif user_total < comp_total:
            print("You lost!")
            print()
        elif user_total == 21:
            print("You win!")
            print()
        elif user_total == comp_total:
            print("You tie!")
            print()

        game_running = False
        user = []
        comp = []