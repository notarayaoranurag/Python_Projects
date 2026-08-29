import random

print("Welcom to ROCK PAPER SCISSORS !!")
signs = ["r","p","s"]
while True :
    player_sign = input("Enter 'R' for rock , 'P' for paper , 'S' for scissors : ")
    if player_sign.lower() == "r" or player_sign.lower() == "p" or player_sign.lower() == "s" :
        computer_sign = (random.randint(1,3))
        position = signs.index(player_sign.lower())
        result = (position - (computer_sign-1)) % 3
        if result ==0 :
            print("Draw!!")
        elif result ==1 :
            print("Player Wins!!")
        else :
            print("Computer Wins!!")
    else :
       print("Please enter something from given option ")
       print("Enter values again")
       continue
    exit = input("Enter 'n' to exit the game : ")
    if exit.lower() == "n" :
        break
