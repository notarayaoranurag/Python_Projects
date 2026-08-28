import random
print("Welcome to Number guessing game the numbers will be 1 - 100 ")
while True :
    random_no = random.randint(1,100)
    guessing =True
    while guessing :
        try:
            guess = int(input("Enter your guessed number from 1 to 100 "))
        except :
            print("You should write a number insted of other character")
            continue
        if guess == random_no :
            print("You guessed it right!!")
            break
        elif guess < 1 or guess > 100 :
            print("Your guess should be less than or equal to 100 and greater than or equal to 1")
            print("guess again")
            continue
        elif guess > random_no :
            if guess < random_no + 10 :
                if guess < random_no + 5 :
                    print("You are tooo close to magic number")
                else :
                    print("Your number is slightely bigger than the magic number")
            else :
                print("Your number is bigger than the magic number")
        else :
            if guess > random_no - 10 :
                if guess > random_no - 5 :
                    print("You are tooo close to magic number")
                else :
                    print("Your number is slightely lower than the magic number")
            else :
                print("Your number is lesser than the magic number")
    play_or_not = input("Type 'n' and then enter to stop the game ")
    if play_or_not.lower() == "n" :
        break
