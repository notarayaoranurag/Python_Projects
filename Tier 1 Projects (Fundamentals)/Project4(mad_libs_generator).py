import random

print("WELCOME TO MAD LIBS STORY !!")
while True :
    noun1 = input("Enter the noun(person/place/thing) : ")
    adjective1 = input("Enter the adjective(describing word) : ")
    verb1 = input("Enter a simple verb : ")
    adjective2 = input("Enter the adjective(describing word) : ")
    plural_noun = input("Enter the Plural noun (noun just for a plural thing) : ")
    color = input("Enter a specific color(red, blue , purple , etc) : ")
    place = input("Enter a specific place(any place) : ")
    verb2 = input("Enter any simple verb : ")
    adjective3 = input("Enter the adjective(defining word) : ")
    noun2 = input("Enter the noun(person/place/thing) : ")
    story_telling = True
    while story_telling :
        which_game = input("We have 3 story type 1 to play story one , 2 for second & 3 for third or you want to randomly chose a game : ")
        if which_game == "r" :
            which_game = random.randint(1,3)
        if str(which_game) == "1" :
            print(f"""Cooking is supposed to be a/an {adjective1} experience,the chef said, holding up a giant {noun1}.
                We will start by {verb1}ing our ingredients.
                Everyone looked nervous because the kitchen smelled very {adjective2}.
                Suddenly, a jar of pickled {plural_noun} exploded, covering the walls in a bright {color} goo.
                It looked like a scene straight out of {place}.
                The chef yelled, {verb2} for your lives!
                It was the most {adjective3} cooking class ever, and we all ended up eating a giant {noun2} for dinner instead.""")
            break
        elif str(which_game) == "2" :
            print(f"""Agent 007 slid down the {adjective1} zipline, tightly clutching a top-secret {noun1}.
                The mission required {verb1}ing past laser grids without being detected.
                The villain's lair was hidden inside a/an {adjective2} mountain fortress, guarded by weaponized {plural_noun}.
                Suddenly, a {color} alarm flashed!
                The evil mastermind appeared on the screen, laughing all the way from {place}.
                "You're too late! Now, I will {verb2} the world!" the villain cackled.
                Thinking fast, the agent threw a/an {adjective3} smoke bomb and escaped inside a giant {noun2}.""")
            break
        elif str(which_game) == "3" :
            print(f"""Our school bus pulled up to the {adjective1} gates of the zoo.
                Our teacher warned us, "Keep an eye out for the rare, wild {noun1}!"
                As we walked through the gates, we saw a group of monkeys {verb1}ing in the trees.
                The tour guide told us that the animals here are incredibly {adjective2} and love to eat {plural_noun}.
                Suddenly, a zebra turned a vibrant shade of {color}  right before our eyes! "Wow, this looks like {place}!" screamed my classmate.
                Right then, a parrot leaned out of its cage to {verb2} at our principal.
                It was a truly {adjective3} field trip, and I even got a souvenir {noun2} to take home!""")
            break
        else :
            print("Please enter a valid input")
            continue
    exit = input("Enter 'n to exit the game : ")
    if exit.lower() == "n" :
        break
