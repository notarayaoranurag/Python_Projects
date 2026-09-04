import random
while True :
    score = 0
    try:
        how_many_dice = int(input("Enter the no. of dice from 1-6 to roll : "))
        how_many_side = int(input("Enter the no. of side's each dice should have from 1-6 : "))
    except :
        print("Please enter a numerical value !!")
        continue
    if 1<=how_many_dice<=6 and 1<=how_many_side<=6 :
        try:
            player_guess = int(input("Guess the score you think will come : "))
        except :
            print("Please enter a integer value!!")
            continue
        for values in range (1,how_many_dice+1) :
            side_values = random.randint(1,how_many_side)
            score += side_values
            print(f"Dice {values} = {side_values}")
        print(f"Total Score is {score}")
        if player_guess == score :
            print("You guessed right !!")
        elif score-3<=player_guess<=score+3 :
            print("You were close !!")
        else :
            print("You guessed wrong !!")
    else :
        print("Please enter a posssible no. of faces or dice !!")
    close_it = input("Enter 'n' to close the program : ")
    if close_it.lower() == "n" :
        break
