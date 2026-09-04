tasks = []
complete_or_not = []
while True :
    print("Your task list is :-")
    for task in range (len(tasks)):
        print(task +1," ",tasks[task]," -> ",complete_or_not[task])
    try:
        what_to_do = int(input("""1 - add tasks
        2 - remove tasks
        3 - add new tasks
        4 - mark certain task complete
        5 - quit
        Enter the task number you want to do : """))
    except :
        print("You need to enter the task number you want to do ")
        continue
    if what_to_do == 1 :
        while True :
            task_to_add = input("Enter The task you want to do : ")
            completed_or_not = input("Enter that is the task is complete or not , just write done or pending : ")
            tasks.append(task_to_add)
            complete_or_not.append(completed_or_not)
            print("Your task list is :-")
            for task in range (len(tasks)):
                print(task +1," ",tasks[task]," -> ",complete_or_not[task])
            writing_task = input("If you are done writing tasks just press n and enter : ")
            if writing_task.lower() == "n" :
                break
    elif what_to_do == 2 :
        while True :
            try :
                task_to_remove = int(input("Enter the task no. you want to remove : "))
            except :
                print("Please enter a number insted of any other character ")
                continue
            if task_to_remove >= 1 and task_to_remove <=len(tasks) :
                tasks.pop(task_to_remove-1)
                complete_or_not.pop(task_to_remove-1)
            else :
                print("Please enter a valid no. ")
                continue
            print("Your task list is :-")
            for task in range (len(tasks)):
                print(task +1," ",tasks[task]," -> ",complete_or_not[task])
            stop_removal = input("If you are done removing tasks just press n and enter : ")
            if stop_removal.lower() == "n" :
                break
    elif what_to_do == 3 :
        while True:
            more_task_to_add = input("Enter tasks you want to add : ")
            complete_or_not_the_new = input("Enter that is the task is complete or not , just write done or pending :  ")
            tasks.append(more_task_to_add)
            complete_or_not.append(complete_or_not_the_new)
            print("Your task list is :-")
            for task in range (len(tasks)):
                print(task +1," ",tasks[task]," -> ",complete_or_not[task])
            stop_appending = input("If you are done adding tasks just press n and enter : ")
            if stop_appending.lower() == "n" :
                break
    elif what_to_do == 4 :
        while True :
            try:
                which_task_to_change = int(input("please enter the the task no. you want to change it's mark "))
                what_to_change_it_into = input("Which mark you want to apply it : ")
            except :
                print("Please enter a valid task number")
                continue
            if which_task_to_change >= 1 and which_task_to_change <= len(tasks) :
                complete_or_not[which_task_to_change-1] = what_to_change_it_into
            else:
                print("Enter a valid no. to assign a mark")
            stop_marking = input("If you are done marking tasks just press n and enter : ")
            if stop_marking.lower() == "n" :
                break
    elif what_to_do == 5 :
        break
    else :
        print("Please enter a given number ")
        continue
