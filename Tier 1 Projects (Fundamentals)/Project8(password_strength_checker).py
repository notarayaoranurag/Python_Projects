import random
while True:
    generated_pass = ""
    upper_case = 0
    random_upper_case_list = ["A","B","C","D"]
    lower_case = 0
    random_lower_case_list = ["d","a","c","b"]
    integer = 0
    special_character = 0
    random_special_character = ["!","@","#","$","%"]
    random_key = random.randint(0,3)
    first_letter_lower_of_upper = 0
    first_letter_upper_of_lower = 0
    usr_pass = input("Enter your password to strength check : ")
    corrected_upper = ""
    corrected_lower = ""
    corrected_integer = ""
    lower_seal = 0
    upper_seal = 0
    integer_seal = 0
    special_seal = 0
    for checking in (usr_pass) :
        if checking.islower() :
            lower_case += 1
            if lower_seal == 0 :
                lower_seal += 1
        elif checking.isupper() :
            upper_case += 1
            if upper_seal == 0 :
                upper_seal += 1
        elif checking.isdigit() :
            integer += 1
            if integer_seal == 0 :
                integer_seal +=1
        elif "!"in checking or "@"in checking or "#"in checking or "$"in checking or "%"in checking or "^"in checking or "&"in checking or "*"in checking or "("in checking or ")"in checking or "-"in checking or "_"in checking or "="in checking or "+"in checking or "/"in checking or "?"in checking or "."in checking or ","in checking or ">"in checking or "<"in checking or ";"in checking or ":"in checking or "]"in checking or "["in checking or "}"in checking or "{" in checking :
            special_character += 1
            if special_seal == 0 :
                special_seal += 1
        else :
            print("Please enter something ")
            continue
    result = lower_seal + upper_seal + integer_seal + special_seal
    if len(usr_pass) >= 8 :
        if upper_case == 0 and lower_case <=1 :
            corrected_upper = random_upper_case_list[random_key] + usr_pass
        elif upper_case == 0 and lower_case > 1 :
            for lower_to_upper in usr_pass :
                if first_letter_lower_of_upper == 0 :
                    if lower_to_upper.islower() :
                        corrected_upper += lower_to_upper.upper()
                        first_letter_lower_of_upper += 1
                    else :
                        corrected_upper += lower_to_upper
                else :
                    corrected_upper += lower_to_upper
        else :
            corrected_upper = usr_pass
        if lower_case == 0 and upper_case <= 1 :
            corrected_lower = random_lower_case_list[random_key] + usr_pass
        elif lower_case == 0 and upper_case > 1 :
            for upper_to_lower in corrected_upper :
                if first_letter_upper_of_lower == 0 :
                    if upper_to_lower.isupper() :
                        corrected_lower += upper_to_lower.lower()
                    else :
                        corrected_lower += upper_to_lower
                else :
                    corrected_lower += upper_to_lower
        else :
            corrected_lower = corrected_upper
        if integer == 0 :
            corrected_integer += corrected_lower + str(random_key)
        else :
            corrected_integer = corrected_lower
        if special_character == 0 :
            generated_pass += corrected_integer + random_special_character[random_key]
        else :
            generated_pass = corrected_integer
        if result == 1 :
            print(f"Your password is very very weak!! your password -> {usr_pass}")
        elif result == 2 :
            print(f"Your password is  weak! your password -> {usr_pass}")
        elif result == 3 :
            print(f"Your password is ok your password -> {usr_pass}")
        elif result == 4 :
            print(f"Your password is good! your password -> {usr_pass}")
        if lower_case == 0 :
            print("You were missing lower case character")
        elif upper_case == 0 :
            print("You were missing upper case character")
        elif integer == 0 :
            print("You were missing numeric value")
        elif special_character == 0 :
            print("You were missing special character")
        print(f"I recomand you this good password ->{generated_pass}")
    else :
        print("Your password length should be 8 or more than 8")
        continue
    stop_password_checker = input("Enter 'n' to Quit the password strength checker : ")
    if stop_password_checker.lower() == "n" :
        break
