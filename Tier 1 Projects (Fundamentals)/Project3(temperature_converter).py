print("TEMPERATURE CONVERTER!")
def c_to_f(input_temp):
    return((input_temp * 9/5) + 32)
def f_to_c(input_temp):
    return((input_temp-32)*5/9)
def c_to_k(input_temp):
    return(input_temp + 273.15)
def k_to_c(input_temp):
    return(input_temp - 273.15)
def f_to_k(input_temp):
    return(((input_temp-32)*5/9) +273.15)
def k_to_f(input_temp):
    return(((input_temp-273.15)*9/5)+32)
while True :
    try :
        input_temp = float(input("Enter the numeric value of the teperature :"))
    except :
        print("You need to enter numeric value!!")
        print("Enter the value again")
        continue
    current_unit = input("Enter Your current unit 'C' for Celsius , 'K' for Kelvin & 'F' for Fahrenheit :")
    to_convert_to = input("Enter according to what you want to convert in 'C' for Celsius , 'K' for Kelvin & 'F' for Fahrenheit :")
    if (current_unit.lower() == "c" or current_unit.lower() == "k" or current_unit.lower() == "f" ) and (to_convert_to.lower() == "c" or to_convert_to.lower() == "k" or to_convert_to.lower() == "f") :
        if current_unit == to_convert_to :
            print("You can't convert to same unit ! ")
            print("Enter the values again !")
            continue
        else :
            if current_unit.lower() == "c" and to_convert_to.lower() == "f" :
                print(input_temp,"° C = ", c_to_f(input_temp),"F")
            elif current_unit.lower() == "c" and to_convert_to.lower() == "k" :
                print(input_temp,"° C = ", c_to_k(input_temp),"K")
            elif current_unit.lower() == "f" and to_convert_to.lower() == "c" :
                print(input_temp," F = ", f_to_c(input_temp),"° C")
            elif current_unit.lower() == "f" and to_convert_to.lower() == "k" :
                print(input_temp," F = ", f_to_k(input_temp)," K")
            elif current_unit.lower() == "k" and to_convert_to.lower() == "c" :
                print(input_temp, " K = ", k_to_c(input_temp),"° C")
            else :
                print(input_temp, " K = ", k_to_f(input_temp)," F")
        exit = input("Enter 'n' to exit the converter :")
        if exit.lower() == "n" :
            break
    else :
        print("unit you have entered is invalid !")
        print("enter the value again")
        continue
