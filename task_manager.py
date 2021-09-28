# import the function date from datetime
from datetime import datetime
from datetime import date
# define the function reg_user()
def reg_user():

    # creat an empty file called username to store user name data
    # Creat an empty file called password to store password data
    username = ""
    password = ""

    # Open user txt file to read the data
    user_file = open("user.txt", "r")

    #use a for loop to loop through the data in the user.txt file
        # Use strip to remove punctuation at the start and end of line and save in variable temp
        # Use split to split the data in each line on the comma into characters
        # Each user name added assign it to temp[o]
        # Each psss word added assign it to temp[1]
    for line in user_file:
        temp = line.strip()
        temp = temp.split(",")
        username += temp[0]
        password += temp[1]

    # Close the file
    user_file.close()

    # Let new_log equal False
    new_log = False

    # Use a while loop for when the newuser already exists in the data base
        # Aske user to enter a new name and save as newuser 
        # Use if statement if the user is alread in the data base
            # Use f string to output newuser exists in the data base                         
            # New_log equals False so the loop will continue
    while new_log == False:
        newuser = input(" Please enter a new name: ")
        if newuser in username:
            print(f" {newuser} exists within the data base ")
            new_log = False
            
        # Use if statement when newuser is not in username
        # Use f string to output newuser does not exist in the data base 
        # New_log equals True so code will exit loop and continue
        if newuser not in username:
            print(f" {newuser} is not in the data base ")
            new_log = True
            
    # Ask user to input a new password and save as newpass
    # Ask the user to confirm the password and save as passconfirm
    newpass = input(" Please enter a new password: ")
    passconfirm = input(" Please re enter your password: ")

    # use if statement when the passconfirm is the same as the newpass
        # open the user.txt file and append data to it
        # using a f string to write the new username to the user text file 
        # using a fstring to write the new password to the user text file
        # Use f string to print the conformation of the new user neing added to the  user text file
        # Close the file                
    if newpass == passconfirm:
        user_file = open("user.txt", "a")
        user_file.write(f" \n{newuser} ,")
        user_file.write(f" {newpass} ")
        print(f" Confirmed: {newuser} has been added to the database") 
        

        # Open user txt file to read the data
        # Use a for loop to loop through the data in the user.txt file
        # Use strip to extract the data line by line and remove any punctuation at the start and end of the line and save in variable temp
        # Use split to split the data in each line at the comma and save it in the variable temp
        # Each user name added assign it to temp[o]
        # Each psss word added assign it to temp[1]
        user_file = open("user.txt", "r")

        for line in user_file:
            temp = line.strip()
            temp = temp.split(",")
            username += temp[0]
            password += temp[1]

        # Close the file
        user_file.close()
        
    # Use else statement if newpass is not the same as passconfirm
    else:
        print(" Your passwords do not match ")

# Define the function add_task()
def add_task():

    # Creat an empty file called username to store username data
    # Creat an empty file called password to store password data
    # Let Task_count equal zero
    username = ""
    password = ""
    
    

    # Open user txt file to read the data
    user_file = open("user.txt", "r")

    #use a for loop to loop through the data in the user.txt file
        # Use strip to remove punctuation at the start and end of line and save in variable temp
        # Use split to split the data in each line on the comma into characters
        # Each user name added assign it to temp[o]
        # Each psss word added assign it to temp[1]
    for line in user_file:
        temp = line.strip()
        temp = temp.split(",")
        username += temp[0]
        password += temp[1]
        
       
    # Close the file
    user_file.close()

    # Let user_log equal False
    user_log = False

  

    # Use a while loop for entering a user to assigne a task to
    # Ask the user to enter a name to assigne the task to and save as variable newuser1 
    # Use if statement when the name is not in the data base
    # Use f string to output newuser1 does not exist in the data base
    # User_log equals false so the while loop will continue
    while user_log == False:
        newuser1 = input(" Please enter a user to assign this task to: ")
        if newuser1 not in username:
            print(f" {newuser1} does not exist within our data base ")
            user_log = False
        
        # Use an if statement when the newuser1 is in the database
        # use f string to output newuser does exist in data base 
        # User_log equals true so the code exits out the while loop and continues
        if newuser1 in username:
            print(f" {newuser1} exists within our data base ")
            user_log = True
            
    # Ask user to enter a new task and save it as newtask
    # Ask user to enter a task description and save as newtaskdes 
    # Use date.today to select todays date and .strftime to output the day, month, year as a string
    # Ask the user to enter the date the task will be complete and save as newdatcom
    # is the task complete will be hard coded as no
    newtask = input(" Please enter a new task: ")
    newtaskdes = input(" Please enter a task description: ")
    newdateass = date.today().strftime("%Y-%m-%d")
    newdatcom = input("Please enter a date the task will be complete yyyy-mm-dd: ")
    newtaskcom = "No"

    # Open the tasks.txt file and append the new data to it
    # Write the task_no the the a new line in the task.txt
    # Write the newuser1 to a new line in task.txt
    # Write the newtask to a new line in tasks.txt
    # Write the newtaskdes to a new line in tasks.txt
    # Write the newdateass to a new line in tasks.txt
    # Write the newdatcom to a new line in tasks.txt
    # Write the newtaskcom to a new line in tasks.txt 
    # Print the new task ahs been assigned to the user
    # Close the file task.txt
    task_file = open("tasks.txt", "a")
    task_file.write(f"{newuser1},")
    task_file.write(f"{newtask},")
    task_file.write(f"{newtaskdes},")
    task_file.write(f"{newdateass},")
    task_file.write(f"{newdatcom},")
    task_file.write(f"{newtaskcom}\n")
    print(f" Confirmed: {newtask} has been assigned to {newuser1} ")
    task_file.close()

# Define the function view_all()
def view_all():

    # Open task txt file to read the data
    # Use a for loop with line  to loop through the data line by line in the task.txt file
        # Use strip to remove the punctuation at the start and end of line and save in variable temp1
        # Use split to split the data in each line on the comma and save it in temp1
        # Print the data in a f string to output the data
    
    tasks_file = open("tasks.txt", "r")
    for line in tasks_file:
        temp1 = line.strip()
        temp1 = temp1.split(",")
        print(f""" Assigned to:             {temp1[0]}
 Task:                    {temp1[1]}
 Date assigned:           {temp1[3]}
 Due date:                {temp1[4]}
 Task Complete?:          {temp1[5]}
 Task Description:        {temp1[2]}\n """)
        
    # Close the file
    tasks_file.close()

# Define the function view_mine
    # Open task file
    # Use readlines to read the lines in the file
    # Let count equal 0
    # Let VmList equal an empty list

def view_mine():
    file_tasks = open("tasks.txt", "r")
    lines = file_tasks.readlines()
    taskNum = 0
    myTask = []

    # Use a for loop with in to loop through the task file
        # Let the different headings equal line and split it with a comma
        # Append line to the vmList list
    for line in lines:
        user, title, description, assignDate, dueDate, completed = line.split(",")
        taskNum += 1
        

        # Use the if function if userLoggin is in user character
            # Let count equal count plus one
            # Print ou the f strings
        if userLoggin in user:
            
            print(f" Task assigned to : {user} ")
            print(f" Task number : {taskNum} ")
            print(f" Task Title : {title} ")
            print(f" Task Discription : {description} ")
            print(f" Task Assigned Date : {assignDate} ")
            print(f" Task Due Date : {dueDate} ")
            print(f" Task Completed : {completed} ")
            myTask.append(line)
            
            
    # Ask user to enter the task number they want to edit
    view_mine_option = input(" \nPlease select a task number to be edited:\n")

    # Use an if ststement if choice equal asking the user to input the number of the task they want to eddit
        # Let taskIndex equal the integer of choice subtract one
        # Let userList equal myTask taskIndex
        # Let userList equal the heading charaters and split it with a comma
    if view_mine_option == "1":
        taskIndex = int(view_mine_option) - 1
        userList = myTask[taskIndex]
        
        user,title,description,assignDate,dueDate,completed = userList.split(",")
        
        if completed == completed.strip("\n"):
            newLine = False
            
        else:
            newLine = True

        completed = completed.strip("\n")
        
        
        # Ask the user to choose to mark task as complete or edit task and save as edit
        edit = input("c -> mark task as complete \ne -> edit task \n: ")
        
        # If user selects c to mark task as complete
            # Use if statement if yes in complete
                # Print task marked as complete
            # Use else statement and let completed equal yes
        if edit == "c":
            if "Yes" in completed:
                print(" This task is already marked as complete ")
            else:
                completed = "Yes"
            
        # If user selects e to edit task
            # Let newUser equal False
            # Use if statement if yes in complete
                # Print task marked as complete
        elif edit == "e":
            newUser = False
            if "Yes" in completed:
                print(" This task is already marked as complete ")

            # Use else statement to ask user to enter new name and date
                # Ask the user to choose to enter a new user or change the date and save as edit
                # Use an if statement if edit equals u
                    # Use while loop to get user to enter name from user file let newUser equal False
                        # open user file, use a for loop and strip and split
            else:
                edit = input("u - edit the user \nd - edit the date \n: ")
                if edit == "u":
                    while newUser == False:
                        newUserAssign = input(" Enter the new user: ")
                        userR = open("user.txt", "r")
                        lines = userR.readlines()
                        for line in lines:
                            temp = line.strip()
                            temp = line.split(",")

                        # Use an if statement if newUserAssign not in user file
                        # Print user not registered
                            # newUser equals False
                        if newUserAssign not in temp[0] or newUserAssign == " ":
                            print(" User not registered ")
                            newUser = False

                        # Use an elif statement if newUserAssign in user file
                            # Print user is registered
                            # newUser equals True 
                        elif newUserAssign in temp[0]:
                            print(" User registered ")
                            newUser = True

                    # Save new name as user
                    # Close user file
                    user = newUserAssign
                    userR.close()

                # Use an elif statement if edit equal d
                # Ask user to enter new date
                # Save new date as duedate
                elif edit == "d":
                    newDate = input(" Enter the new date (use the format yyyy-mm-dd) : ")
                    dueDate = newDate

        if newLine == True:
            completed += "\n"

        # Final is the f string
        final = f"{user},{title},{description},{assignDate},{dueDate},{completed}"
    
        # Let newTask = userList at taskIndex
        newTask = userList[taskIndex]
        indexTask = 0

        # Use a for loop to loop through the newTask
            # Use an if statement if lines equals i
                # newTask at indexTask equals final
        for i in newTask:
            if lines == i:
                newTask[indexTask] = final

            # IndexTask equal indexTask plus one
            indexTask += 1
        
        # Open tasks text file and save as g
        # Let a equal first line in text file
        # Let b equal second line in text file
        # Let c equal third line in text file
        g = open("tasks.txt", "r")
        a = (g.readline())
        b = (g.readline())
        c = (g.readline())
        d = (g.readline())
        
        # Let f equal open the tasks.txt file and write
        # write final into the tasks.txt file
        
        with open("tasks.txt", "w") as f:
            f.write(f"{final}")

        # Let h equal open the tasks.txt file and append
        # write b into the tasks.txt file
        with open("tasks.txt", "a") as f:
            f.write(f"{b}")
        # Let k equal open the tasks.txt file and append
        # write c into the tasks.txt file
        with open("tasks.txt", "a") as f:
               f.write(f"{c}")

        # Let p equal open the tasks.txt file and append
        # write c into the tasks.txt file
        with open("tasks.txt", "a") as f:
               f.write(f"{d}")

        #Close file
        f.close()
        g.close()

    # Use the elif function if choice equals 2
        # Let index equal the integer of choice subtract one
        # Let userList equal myTask index
        # Let line equal the heading charaters and split it with a comma
    elif view_mine_option == "2":
        taskIndex = int(view_mine_option) - 1
        userList = myTask[taskIndex]
        print(userList)
        user,title,description,assignDate,dueDate,completed = userList.split(",")

        if completed == completed.strip("\n"):
            newLine = False
            
        else:
            newLine = True

        completed = completed.strip("\n")
    
        # Ask the user to choose to mark task as complete or edit task and save as edit
        edit = input("c -> mark task as complete \ne -> edit task \n: ")
        
        # If user selects c to mark task as complete
            # Use if statement if yes in complete
                # Print task marked as complete
            # Use else statement and let completed equal yes
        if edit == "c":
            if "Yes" in completed:
                print(" This task is already marked as complete ")
            else:
                completed = "Yes" 
            
        # If user selects e to edit task
            # Let newUser equal False
            # Use if statement if yes in complete
                # Print task marked as complete
        elif edit == "e":
            newUser = False
            if "Yes" in completed:
                print(" This task is already marked as complete ")

            # Use an else statement
                # Ask the user to choose to enter a new user or change the date and save as edit
                # Use an if statement if edit equals u
                    # Use while loop to get user to enter name from user file let newUser equal False
                        # open user file, use a for loop and strip and split
            else:
                edit = input("u - edit the user \nd - edit the date \n: ")
                if edit == "u":
                    while newUser == False:
                        newUserAssign = input(" Enter the new user: ")
                        userR = open("user.txt", "r")
                        lines = userR.readlines()
                        for line in lines:
                            temp = line.strip()
                            temp = line.split(",")

                        # Use an if statement if newUserAssign not in user file
                            # Print user not registered
                            # newUser equals False
                        if newUserAssign not in temp[0] or newUserAssign == " ":
                            print(" User not registered ")
                            newUser = False

                        # Use an if statement if newUserAssign in user file
                            # Print user is registered
                            # newUser equals True 
                        elif newUserAssign in temp[0]:
                            print(" User registered ")
                            newUser = True

                    # Save new name as user
                    # Close user file
                    user = newUserAssign
                    userR.close()

                # Use an elif ststement if edit equals d
                    # Ask user to enter new date
                    # Save new date as duedate
                elif edit == "d":
                    newDate = input(" Enter the new date (use the format yyyy-mm-dd) : ")
                    dueDate = newDate

        if newLine == True:
            completed += "\n"

        # Final is the f string
        final = f"{user},{title},{description},{assignDate},{dueDate},{completed}"
    
        # Let newTask = userList at taskIndex
        newTask = userList[taskIndex]
        indexTask = 0

        # Use a for loop to loop through the newTask
            # Use an if statement if lines equals i
                # newTask at indexTask equals final
        for i in newTask:
            if lines == i:
                newTask[indexTask] = final

            # IndexTask equal indexTask plus one
            indexTask += 1

        # Open tasks text file and save as g
        # Let a equal first line in text file
        # Let b equal second line in text file
        # Let c equal third line in text file     
        g = open("tasks.txt", "r")
        a = (g.readline())
        b = (g.readline())
        c = (g.readline())
        d = (g.readline())
        
        

        

        # Let f equal open the tasks.txt file and write
        # write final into the tasks.txt file
        # Close the tasks.txt file
        with open("tasks.txt", "w") as f:
            f.write(f"{final}")

        # Let f equal open the tasks.txt file and append
        # write a into the tasks.txt file
        with open("tasks.txt", "a") as f:
            f.write(f"{a}")

        # Let f equal open the tasks.txt file and append
        # write c into the tasks.txt file
        with open("tasks.txt", "a") as f:
            f.write(f"{c}")

        # Let f equal open the tasks.txt file and append
        # write d into the tasks.txt file
        with open("tasks.txt", "a") as f:
            f.write(f"{d}")
        
        #Close file
        f.close()
        g.close()

    # Use an if ststement if choice equal asking the user to input the number of the task they want to eddit
        # Let taskIndex equal the integer of choice subtract 3
        # Let userList equal myTask taskIndex
        # Let userList equal the heading charaters and split it with a comma 
    if view_mine_option == "3":
        taskIndex = int(view_mine_option) - 3
        userList = myTask[taskIndex]
        print(userList)
        user,title,description,assignDate,dueDate,completed = userList.split(",")
        
        if completed == completed.strip("\n"):
            newLine = False
            
        else:
            newLine = True

        completed = completed.strip("\n")
        
        
        # Ask the user to choose to mark task as complete or edit task and save as edit
        edit = input("c -> mark task as complete \ne -> edit task \n: ")
        
        # If user selects c to mark task as complete
            # Use if statement if yes in complete
                # Print task marked as complete
            # Use else statement and let completed equal yes
        if edit == "c":
            if "Yes" in completed:
                print(" This task is already marked as complete ")
            else:
                completed = "Yes"
            
        # If user selects e to edit task
            # Let newUser equal False
            # Use if statement if yes in complete
                # Print task marked as complete
        elif edit == "e":
            newUser = False
            if "Yes" in completed:
                print(" This task is already marked as complete ")

            # Use else statement to ask user to enter new name and date
                # Ask the user to choose to enter a new user or change the date and save as edit
                # Use an if statement if edit equals u
                    # Use while loop to get user to enter name from user file let newUser equal False
                        # open user file, use a for loop and strip and split
            else:
                edit = input("u - edit the user \nd - edit the date \n: ")
                if edit == "u":
                    while newUser == False:
                        newUserAssign = input(" Enter the new user: ")
                        userR = open("user.txt", "r")
                        lines = userR.readlines()
                        for line in lines:
                            temp = line.strip()
                            temp = line.split(",")

                        # Use an if statement if newUserAssign not in user file
                        # Print user not registered
                            # newUser equals False
                        if newUserAssign not in temp[0] or newUserAssign == " ":
                            print(" User not registered ")
                            newUser = False

                        # Use an elif statement if newUserAssign in user file
                            # Print user is registered
                            # newUser equals True 
                        elif newUserAssign in temp[0]:
                            print(" User registered ")
                            newUser = True

                    # Save new name as user
                    # Close user file
                    user = newUserAssign
                    userR.close()

                # Use an elif statement if edit equal d
                # Ask user to enter new date
                # Save new date as duedate
                elif edit == "d":
                    newDate = input(" Enter the new date (use the format yyyy-mm-dd) : ")
                    dueDate = newDate

        if newLine == True:
            completed += "\n"

        # Final is the f string
        final = f"{user},{title},{description},{assignDate},{dueDate},{completed}"
    
        # Let newTask = userList at taskIndex
        newTask = userList[taskIndex]
        indexTask = 0

        # Use a for loop to loop through the newTask
            # Use an if statement if lines equals i
                # newTask at indexTask equals final
        for i in newTask:
            if lines == i:
                newTask[indexTask] = final

            # IndexTask equal indexTask plus one
            indexTask += 1
        
        # Open tasks text file and save as g
        # Let a equal first line in text file
        # Let b equal second line in text file
        # Let c equal third line in text file
        g = open("tasks.txt", "r")
        a = (g.readline())
        b = (g.readline())
        c = (g.readline())
        d = (g.readline())
        
        # Let f equal open the tasks.txt file and write
        # write final into the tasks.txt file
        
        with open("tasks.txt", "w") as f:
            f.write(f"{final}")

        # Let h equal open the tasks.txt file and append
        # write a into the tasks.txt file
        with open("tasks.txt", "a") as f:
            f.write(f"{a}")
        # Let k equal open the tasks.txt file and append
        # write b into the tasks.txt file
        with open("tasks.txt", "a") as f:
               f.write(f"{b}")

        # Let p equal open the tasks.txt file and append
        # write d into the tasks.txt file
        with open("tasks.txt", "a") as f:
               f.write(f"{d}")
        #Close file
        f.close()
        g.close()
    
    # Use an if ststement if choice equal asking the user to input the number of the task they want to eddit
        # Let taskIndex equal the integer of choice subtract 4
        # Let userList equal myTask taskIndex
        # Let userList equal the heading charaters and split it with a comma 
    if view_mine_option == "4":
        taskIndex = int(view_mine_option) - 4
        userList = myTask[taskIndex]
        print(userList)
        user,title,description,assignDate,dueDate,completed = userList.split(",")
        
        if completed == completed.strip("\n"):
            newLine = False
            
        else:
            newLine = True

        completed = completed.strip("\n")
        
        
        # Ask the user to choose to mark task as complete or edit task and save as edit
        edit = input("c -> mark task as complete \ne -> edit task \n: ")
        
        # If user selects c to mark task as complete
            # Use if statement if yes in complete
                # Print task marked as complete
            # Use else statement and let completed equal yes
        if edit == "c":
            if "Yes" in completed:
                print(" This task is already marked as complete ")
            else:
                completed = "Yes"
            
        # If user selects e to edit task
            # Let newUser equal False
            # Use if statement if yes in complete
                # Print task marked as complete
        elif edit == "e":
            newUser = False
            if "Yes" in completed:
                print(" This task is already marked as complete ")

            # Use else statement to ask user to enter new name and date
                # Ask the user to choose to enter a new user or change the date and save as edit
                # Use an if statement if edit equals u
                    # Use while loop to get user to enter name from user file let newUser equal False
                        # open user file, use a for loop and strip and split
            else:
                edit = input("u - edit the user \nd - edit the date \n: ")
                if edit == "u":
                    while newUser == False:
                        newUserAssign = input(" Enter the new user: ")
                        userR = open("user.txt", "r")
                        lines = userR.readlines()
                        for line in lines:
                            temp = line.strip()
                            temp = line.split(",")

                        # Use an if statement if newUserAssign not in user file
                        # Print user not registered
                            # newUser equals False
                        if newUserAssign not in temp[0] or newUserAssign == " ":
                            print(" User not registered ")
                            newUser = False

                        # Use an elif statement if newUserAssign in user file
                            # Print user is registered
                            # newUser equals True 
                        elif newUserAssign in temp[0]:
                            print(" User registered ")
                            newUser = True

                    # Save new name as user
                    # Close user file
                    user = newUserAssign
                    userR.close()

                # Use an elif statement if edit equal d
                # Ask user to enter new date
                # Save new date as duedate
                elif edit == "d":
                    newDate = input(" Enter the new date (use the format yyyy-mm-dd) : ")
                    dueDate = newDate

        if newLine == True:
            completed += "\n"

        # Final is the f string
        final = f"{user},{title},{description},{assignDate},{dueDate},{completed}"
    
        # Let newTask = userList at taskIndex
        newTask = userList[taskIndex]
        indexTask = 0

        # Use a for loop to loop through the newTask
            # Use an if statement if lines equals i
                # newTask at indexTask equals final
        for i in newTask:
            if lines == i:
                newTask[indexTask] = final

            # IndexTask equal indexTask plus one
            indexTask += 1
        
        # Open tasks text file and save as g
        # Let a equal first line in text file
        # Let b equal second line in text file
        # Let c equal third line in text file
        g = open("tasks.txt", "r")
        a = (g.readline())
        b = (g.readline())
        c = (g.readline())
        d = (g.readline())
        
        # Let f equal open the tasks.txt file and write
        # write final into the tasks.txt file
        
        with open("tasks.txt", "w") as f:
            f.write(f"{final}")

        # Let h equal open the tasks.txt file and append
        # write a into the tasks.txt file
        with open("tasks.txt", "a") as f:
            f.write(f"{a}")
        # Let k equal open the tasks.txt file and append
        # write b into the tasks.txt file
        with open("tasks.txt", "a") as f:
               f.write(f"{b}")

        # Let p equal open the tasks.txt file and append
        # write c into the tasks.txt file
        with open("tasks.txt", "a") as f:
               f.write(f"{c}")
        #Close file
        f.close()
        g.close()

    # Use elif statement if user enters -1
    elif view_mine_option == "-1":
        print("You have chosen to exit")

# Define the function generate reports         
def generate_reports():
    # Let count equal zero
    # Open tasks file
    # Use for loop with strip and split
        # let count equal count plus on in the for loop
    count = 0
    file = open("tasks.txt", "r")
    lines = file.readlines()
    for line in lines:
        temp = line.strip()
        temp = temp.split(",")
        count = count + 1
     
    # use f string in statement
    # Print statement
    total_num = (f"The total number of tasks is: {count} ")
    print(total_num)

    # Open task overview file and save as f
        # Write total_num to file
    with open("task_overview.txt", "w") as f:
        f.write(total_num)

    # Let n equal yes
    # Let count equal zero
    # Open tasks file
    # Use for loop with strip and split
        # Use if statement if yes in line of file
            # let count equal count plus one in the for loop
    n = "Yes"
    count = 0
    file = open("tasks.txt", "r")
    lines = file.readlines()
    for line in lines:
        temp = line.strip()
        temp = temp.split(",")
        if n in temp[5]:
            count = count + 1

    # use f string in statement
    # Print statement
    com_tasks = (f"The total number of completed tasks is: {count} ")
    print(com_tasks)

    # Open task overview file and save as f
        # Write total_num to file
    with open("task_overview.txt", "a") as f:
        f.write(f"\n{com_tasks} ")

    # Let n equal No
    # Let countN equal zero
    # Open tasks file
    # Use for loop with strip and split
        # Use if statement if no in line of file
            # let countN equal countN plus one in the for loop
    a = "No"
    countN = 0
    file = open("tasks.txt", "r")
    lines = file.readlines()
    for line in lines:
        temp = line.strip()
        temp = line.split(",")
        if a in temp[5]:
            countN = countN + 1

    # use f string in statement
    # Print statement
    Ncom_tasks = (f"The total number of uncompleted tasks is :{countN} ")
    print(Ncom_tasks)

    # Open task overview file and save as f
        # Write total_num to file
    with open("task_overview.txt", "a") as f:
        f.write(f"\n{Ncom_tasks} ")

    # Let c equal No
    # Let count equal zero
    # Let today equal todays date
    # Open tasks file
    # Use for loop with strip and split
        # Use if statement if due date in file is less than or equal to tadays date and no in line of file
            # let count equal count plus one in the for loop
    c = "No"
    count = 0
    file = open("tasks.txt", "r")
    lines = file.readlines()
    today = datetime.today()
    for line in lines:
        temp = line.strip()
        temp = temp.split(",")
        if datetime.strptime(temp[4],"%Y-%m-%d") <= today and c in temp[5]:
            count = count +1
    # use f string in statement
    # Print statement
    ND_tasks = (f"The total number of uncompleted tasks which are overdue is : {count} ")
    print(ND_tasks)

    # Open task overview file and save as f
        # Write ND_tasks to file
    with open("task_overview.txt", "a") as f:
        f.write(f"\n{ND_tasks} ")

    # Let n equal No
    # Let count equal zero
    # Let countT equal zero
    # Open tasks file
    # Use for loop with strip and split
        # Let countT equal countT plus one
        # Use if statement if no in line of file
            # Let count equal count plus one in the for loop
            # Let PtotalN equal count devided by countT and then multiplied by 100
            # Let PtotalN equal the rounded off to an integer value of PtotalN
    a = "No"
    count = 0
    countT = 0
    file = open("tasks.txt", "r")
    lines = file.readlines()
    for line in lines:
        temp = line.strip()
        temp = temp.split(",")
        countT = countT + 1
        if a in temp[5]:
            count = count + 1   
    PtotalN = (count/countT) * 100
    PtotalN = round(PtotalN)

    # use f string in statement
    # Print statement
    per_task_n = (f"The percentage of tasks not complete is: {PtotalN} ")
    print(per_task_n)

    # Open task overview file and save as f
        # Write per_task_n to file
    with open("task_overview.txt", "a") as f:
        f.write(f"\n{per_task_n} ")

    # Let count equal zero
    # Let countT equal zero
    # Let today equal todays date
    # Open tasks file
    # Use for loop with strip and split
        # Let countT equal countT plus one
        # Use if statement if due date in file is less than or equal to tadays date
            # let count equal count plus one in the for loop
            # Let PtotalO equal count devided by countT and then multiplied by 100
            # Let PtotalO equal the rounded off to an integer value of PtotalN 
    count = 0
    countT = 0
    file = open("tasks.txt", "r")
    lines = file.readlines()
    today = datetime.today()

    for line in lines:
        temp = line.strip()
        temp = temp.split(",")
        countT = countT + 1
        if datetime.strptime(temp[4],"%Y-%m-%d") <= today:
            count = count + 1
    PtotalO = (count/countT) * 100
    PtotalO = round(PtotalO)

    # use f string in statement
    # Print statement
    per_task_o = (f"The percentage of tasks which are overdue is : {PtotalO}\n")
    print(per_task_o) 

    # Open task overview file and save as f
        # Write per_task_o to file
    with open("task_overview.txt", "a") as f:
        f.write(f"\n{per_task_o} ")

    # Ask user to input which user they want to work with and save as user
    # Write a f string to output and print
    # Open task overview file and save as f
        # Write per_task_o to file
    user = input(" Please enter the user you wish to work with: ")
    userT =(f"The tasks for {user} is:") 
    print(userT)
    with open("user_overview.txt", "a") as f:
        f.write(f"{userT}")
    
    # Let count equal zero
    # Open tasks file
    # Use for loop with strip and split
        # let count equal count plus on in the for loop
    count = 0
    file = open("tasks.txt", "r")
    line = file.readlines()
    for line in lines:
        temp = line.strip()
        temp = temp.split(",")
        if user in temp[0]:
            count = count + 1

    # use f string in statement
    # Print statement    
    tasks = (f"The total number of tasks for this user is: {count}")
    print(tasks)

    # Open user overview file and save as f
        # Write users to file
    with open("user_overview.txt", "a") as f:
        f.write(f"\n{tasks} ")

    # Let count equal zero
    # Let countT equal zero
    # Open tasks file
    # Use for loop with strip and split
        # let count equal count plus on in the for loop
        # Let Ptotal equal count devided by countT and then multiplied by 100
            # Let Ptotal equal the rounded off to an integer value of Ptotal
    count = 0
    countT = 0
    file = open("tasks.txt", "r")
    line = file.readlines()
    for line in lines:
        temp = line.strip()
        temp = temp.split(",")
        countT = countT + 1
        if user in temp[0]:
            count = count + 1
    Ptotal = (count/countT) * 100
    Ptotal = round(Ptotal)

    # use f string in statement
    # Print statement 
    total_num = (f"The percentage of tasks for this user is: {Ptotal} ")
    print(total_num)

    # Open user overview file and save as f
        # Write users to file
    with open("user_overview.txt", "a") as f:
        f.write(f"\n{total_num} ")

    # Let a equal yes
    # Let count equal zero
    # Let countT equal zero
    # Open tasks file
    # Use for loop with strip and split
        # let countT equal countT plus one
        # Use if statement if yes in line of file and user in line of file
            # Let count equal count plus one in the for loop
    a = "Yes"
    count = 0
    countT = 0
    file = open("tasks.txt", "r")
    lines = file.readlines()
    for line in lines:
        temp = line.strip()
        temp = temp.split(",")
        countT = countT + 1
        if user in temp[0] and a in temp[5] :
            count = count + 1
    # Let Ptotal equal count devided by countT and then multiplied by 100
    # Let Ptotal equal the rounded off to an integer value of Ptotal
    Ptotal = (count/countT) * 100
    Ptotal = round(Ptotal)

    # use f string in statement
    # Print statement
    per_taskY = (f"The percentage of tasks complete for this user is: {Ptotal} ")
    print(per_taskY) 

    # Open user overview file and save as f
        # Write per_tasks to file
    with open("user_overview.txt", "a") as f:
        f.write(f"\n{per_taskY}") 

    
    # Let a equal no
    # Let count equal zero
    # Let countT equal zero
    # Open tasks file
    # Use for loop with strip and split
        # let countT equal countT plus one
        # Use if statement if no in line of file and user in line of file
            # Let count equal count plus one in the for loop
            # Let PtotalN equal count devided by countT and then multiplied by 100
            # Let PtotalN equal the rounded off to an integer value of PtotalN
    b = "No"
    count = 0
    countT = 0
    file = open("tasks.txt", "r")
    lines = file.readlines()
    for line in lines:
        temp = line.strip()
        temp = temp.split(",")
        countT = countT + 1
        if user in temp[0] and b in temp[5] :
            count = count + 1
    PtotalN = (count/countT) * 100
    PtotalN = round(PtotalN)

    # use f string in statement
    # Print statement
    per_taskN = (f"The percentage of tasks not complete for this user is: {PtotalN} ")
    print(per_taskN)

    with open("user_overview.txt", "a") as f:
        f.write(f"\n{per_taskN}")

    c = "No"
    count = 0
    countT = 0
    file = open("tasks.txt", "r")
    lines = file.readlines()
    today = datetime.today()
    for line in lines:
        temp = line.strip()
        temp = temp.split(",")
        if user in temp[0]:
            countT = countT + 1
        if datetime.strptime(temp[4],"%Y-%m-%d") <= today and c in temp[5]:
            count = count +1
    PtotalN = (count/countT) * 100
    PtotalN = round(Ptotal)
    ND_tasks = (f"The percentage of uncompleted tasks for this user which are overdue is : {PtotalN} ")
    print(ND_tasks)

    # Open user overview file and save as f
        # Write ND_tasks to file
    with open("user_overview.txt", "a") as f:
        f.write(f"\n{ND_tasks}\n")

    file.close()
    f.close()
    
    
#Define the function statistics()
def statistics():
    
    
    # Print statement
    # Open the task.txt file and save it as the variable task_file
    # Use a for loop to loop through the data line by line in the task.txt file 
        # Use strip to remove punctuation at the start and the end of the line save in variable temp
        # print temp
    print("Task Overview: ")
    tasks_file = open("task_overview.txt", "r")
    lines = tasks_file.readlines()
    for line in lines:
            temp = line.strip()
            print(temp)
            
    # Print statement
    # Open the task.txt file and save it as the variable task_file
    # Use a for loop to loop through the data line by line in the task.txt file 
        # Use strip to remove punctuation at the start and the end of the line save in variable temp
        # print temp
    print("\nUser Overview: ")
    tasks_file = open("user_overview.txt", "r")
    lines = tasks_file.readlines()
    for line in lines:
            temp = line.strip()
            
            print(temp)
    
    # Close file
    tasks_file.close()



# let LoggedIn equal False
loggedIn = False

# Creat an empty file called username to store username data
# Creat an empty file called password to store password data
username = ""
password = ""

# Open user txt file to read the data
user_file = open("user.txt", "r")

#use a for loop to loop through the data in the user.txt file
# Use strip to remove punctuation at the start and end of line and save in variable temp
# Use split to separate the charaters on each line with a comma and save in the variable temp
# Each user name added assign it to temp[o]
# Each psss word added assign it to temp[1]
for line in user_file:
    temp = line.strip()
    temp = temp.split(",")
    username += temp[0]
    password += temp[1]



# Close the file
user_file.close()

# Use a while loop and let it equal False for incorrect username or password
while loggedIn == False:
    
    # Aske user to enter a user name and save as userLoggin
    # Ask user to enter a pass word and save as userPass
    userLoggin = input(" Please enter your username: ")
    userPass = input(" Please enter your password: ")

    # Use an if statement with not in if user name is not stored in username or user uses a space
    # Print statement 
    # LoggedIn is still False so the loop will still run
    if userLoggin not in username or userLoggin == " ":
        print(" Username not found ")
        loggedIn = False

    # Use elif statement if pass word is not stored in password or user uses a space
    elif userPass not in password or userPass == " ":
        
        print(" Incorrect password ")
        # LoggedIn still False so the while loop will still run 
        loggedIn = False

    # Use elif statement with in, if user name and pass word are stored in username and password
    # LoggedIn is now True so the code exits the loop
    elif userLoggin in username and userPass in password:
        print(f" Welcome {userLoggin} you are logged in ")
        loggedIn = True
    
# Use a while loop for loggin to be true so the code will loop back to the list
while loggedIn == True:

    # use an if statement for when the user inputs admin
        # Print a statement where the user has the choice to add a new user
    if userLoggin == "admin":
        
        print("""\nPlease make a selection from the following:
 r - register a new user
 a - assign a new task
 va - viewall user assigned tasks
 vm - view my assigned tasks
 gr - generate reports
 ds - display statistics
 e - exit """)

    # Use else statement to print a statement where the user can not register a new user    
    else:
       print(""" Please make a selection from the following:
 a - assign a new task
 va - viewall user assigned tasks
 vm - view my assigned tasks
 e - exit """) 
        
    # choice is saved as the choice the user inputs
    choice = input(" ")
    
    # Use the if statement if the user enters r as the choice
        # Call the function
    if choice == "r":
        reg_user()
        
        

    # Use the if statement if the user enters a as the choice
        # Call the function
    if choice == "a":
        add_task()
    
    # Use if statement when user enters va
        # Call the function
    if choice == "va":
        view_all()
        

    # Use if statement when user enters vm
        # Call the function
    if choice == "vm":
        view_mine()
        
    if choice == "gr":
        generate_reports()

    # Use if statement if user enters ds
        # Print choice statement
        # Let choice equal input
        
    if choice == "ds":
        print(f""" Do you wish to generate reports:
        y - Yes
        n - No """)
        choice = input(" ")

        # Use if statement if statement if choice equals yes
        # Call the function generate reports
        # Call the function statistics
        if choice == "y":
            generate_reports()
            statistics()

        # Use elif statement if choice equals n
        # Call the function statistics
        elif choice == "n":
            statistics()
        
            
    # Use the if statement when the user selects e to exit the program 
        # Print a f string to output user is exiting code
        #LoggedIn equals False will exit the code
    if choice == "e":
        print(f" Cofirmed {userLoggin} exiting program ")
        loggedIn = False
         
            
        
