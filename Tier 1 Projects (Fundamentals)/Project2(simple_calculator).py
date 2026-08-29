print("BASIC CALCULATOR!")
print("Instruction - You need to write first number and then the second after that enter the specific sign you were asked for.")
def add(no1,no2):
    return(no1+no2)
def multiply(no1,no2):
    return(no1*no2)
def devide(no1,no2):
    return(no1/no2)
def subtract(no1, no2):
    return(no1-no2)
while True :
    try:
        no1 = float(input("Enter first number  : "))
    except :
        print("Plese enter a number ")
        print("Enter the number again")
        continue
    try:
        no2 = float(input("Enter second number  : "))
    except :
        print("Plese enter a number ")
        print("Enter the number again")
        continue
    sign = input("Enter one of these sign - '+' 'x' '/' '-'")
    if sign == "+" or sign == "x" or sign == "*" or sign == "/" or sign == "-" :
        if sign == "+" :
            print("There result is = ",add(no1 , no2))
        elif sign == "x" or sign == "*" :
            print("There result is = ",multiply(no1,no2))
        elif sign == "/" :
            if no2 == 0 :
                print("UNDEFINED")
            else :
                print("There result is = ", devide(no1,no2))
        elif sign == "-" :
            print("There result is = ",subtract(no1 ,no2))
        exit = input("To exit calculator type 'n'  -")
        if exit.lower() == "n" :
            break
    else :
        print("The sign you entered was invalid")
