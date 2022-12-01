# L1T24
# capstone

# Hi there thanks for the review, The issue was white space in the task.txt file
# the loop was trying to find indexs in blank lines. 
# shoud be fine now, Thanks. 

users_task_dict = {}
users_task_list = []
username_list = []
new_task_file = []
#=====importing libraries=========== 
from datetime import date
from datetime import datetime
import sys
import os.path

#=====functions===================== 
def reg_user():
    # strat by creating a list of users with information from the
    # users document
    with open('user.txt', 'r') as users:
        for lines in users:
            username_list.append(lines.split(',')[0])
    # request a username and then check all lines in username_list
    # for a match
    # start with a process to ensure the new username is unique
    username_taken = True
    while username_taken:
            new_user = input("Please enter an original username:\n")
            if new_user in username_list:
                print('This username already exists')
                # once a valid username is entered 
                # original_username becomes true and closes the loop
            else:
                print('Username accepted.\n')
                username_taken = False      
    new_password = input(f"Please enter a password for {new_user}: ")
                # password must be confirmed
    password_confirm = input("Please Confrim your password: ")
                # if the password_confirm string does not equal new_password exactly
                # request confirmation again
    while new_password != password_confirm:
        password_confirm = input("\n- These passwords do not match -\n"
                            + "Please retype your password to try again: ")
    # once a passwrod has been accepted the info can be added to user.txt
    with open("user.txt", "a") as user_info:
        user_info.write(f"{new_user}, {password_confirm}\n")
         # confirm success to user
    return(print("\nNew user has been successfully added."
            +" What would you like to do next:\n "))


def add_task():
    # reset the user confirmed variables ready for re use
    username_required = True
    # request input from user for the inteded user
    # validate user againdt user.txt
    # reset user_confirmed to ture upon success
    while username_required:
        with open('user.txt', 'r') as users:
            user_allocation = input(
                'Please enter the username of the'
                +'person this task is to be assign to:\n')
            for lines in users:
                if user_allocation in lines:
                        print('User confirmed.')
                        username_required = False
                        user = lines.split(', ')[0]
        # once confirmed create a new list for collecting data
        # add confirmed user to start of list
        new_task = [user,]
        # request relevant information and add to list
        new_task.append(input(
            "Please enter the Title of the task to be completed.\n"))
        new_task.append(input(
            "Please enter a brief desctiption of the task.\n"))
        new_task.append(
            date.today().strftime("%d-%b-%Y").replace("-", " "))
        new_task.append(input(
            "When is this task due?: enter as: DD Mon YYYY\n"))
        new_task.append('No')
        # once list is complete write list to task.txt
        with open('tasks.txt', 'a') as tasks:
            tasks.write("\n")
            tasks.write(', '.join(new_task))
        #notify user of success
            return(print("\n - Task entered successfully -\n"
                        +"What would you like to do next? \n"))


def view_all():
    print('\nThe following tasks are on record:\n')
        #open task.txt and print each line in a readable manner
    with open("tasks.txt", "r") as tasks:
        for lines in tasks:
            # this if statment will exclude any lines that are incpmlete or 
            # accidental such as accidental returns etc
            if len(lines) > 5:
                info_list = lines.split(", ")  # split the lines into index's
                # print out information in appropriate format
                # using relevent index's
                (print(f"Task:             {info_list[1]}\n"
                + f"Assigned to:      {info_list[0]}\n"
                + f"Date assigned:    {info_list[3]}\n"
                + f"Due Date:         {info_list[4]}\n"
                + f"Task Complete:    {info_list[5]}"
                + f"Task Description:\n {info_list[2]}.\n"))
    return(print('\nDone\n'))


def view_my(username):
    ''' start by opening the task file and iterate through the lines
    pulling all lines the have the current users usersame
    all other lines must be added to a new_task_file ready for 
    re pritning the file, otherwise they will be lost.
    '''
    with open("tasks.txt", "r") as tasks:
        for lines in tasks:
            # if the username exists add it to the list 
            if username in lines:  # if the username exists on the line
                users_task_list.append(lines)
            # if the username is not presnet then add the line
            # straght to the new_task_file list
            else:
                new_task_file.append(lines)
    # convert each task into a dictionary value with the key as a 
    # number ready for referencing
    for count, task in enumerate(users_task_list,1):
            users_task_dict[count] = (task.replace('\n', ''))
    # for each dictionary key, pull the value and split it into a list
    for x in users_task_dict.keys():
        info = str(users_task_dict[x])
        info = info.split(', ')
        # print the info from the newly made list using indexs to isolate
        # the information
        print(
        f"\nTask number:      {x}\n"
        + f"Task:             {info[1]}\n"
        + f"Assigned to:      {info[0]}\n"
        + f"Date assigned:    {info[3]}\n"
        + f"Due Date:         {info[4]}\n"
        + f"Task Complete:    {info[5]}\n"
        + f"Task Description:\n {info[2]}.\n")
    # ask the user if any changes are to be made
    task_to_alter = int(input('if you would like to alter a task please enter'
    +' the corresponding task number or else enter -1 to exit\n'))

    # make sure the program is selecting the correct dictionary index
    # even though the keys start at 1 the index still start at 0
    task_to_alter = task_to_alter -1
    # check the specified task exists
    if task_to_alter in range (0, len(users_task_dict)):
        # use the keys in the dictionary to isolate the specified task
        keys = users_task_dict.keys()
        ''' iterate through the keys, 
        any keys that are not required for changing are added
        straight to the new_task_file list ready for printing
        the specified task for changing is sent to the
        task_alterations function
        '''
        for keys in users_task_dict:
            if keys == task_to_alter + 1:  # return to key value
                task_alterations(task_to_alter)
            else:
                new_task_file.append(users_task_dict[keys])
        '''once all the tasks are in the new_task_file list 
        (this includes the altered one which is added 
        in the alterations function)
        the new_task_file can be printed to the 
        tasks.txt overwriting it with the new info
        '''
        with open('tasks.txt', 'w') as task_doc:
            task_doc.write('\n'.join(new_task_file))
        '''if the user chooses to exit no action is required
        as no changes have been made and tasks.txt doc will stay in tact
        the elif statement responds to -2 because -1 -1 = -2
        this is in response to me changing the user input to obtain indexs
        instead of the doctionary keys.
        '''
    elif task_to_alter == -2:
        print('Thank you')
    # if the task is not in range the program will skip back to the main
    # menu and the tasks.txt doc will stay in tact.
    else:
        print('\nSorry this task does not exist.\n')

def task_alterations(x):
    # for the functions to work the task_to_alter needs to be returned to 
    # to the relevant task_dict key number. not index number
    x = x + 1
    # create a list that holds tasks information for isolating indexs
    task = str(users_task_dict[x]).split(', ')
    # first check if the task is compelete
    # if so it cannot be changed
    if task[5] == 'Yes':
        # task must still be re add to new file data
        # other wise it will not appear on the new version
        new_task_file.append(users_task_dict[x])
        output = ('\nComplete Tasks Cannot be ameneded.\n')
    # if the task is not complete the function can be continued
    else:
        # the user is presented with a menu
        alteration = int(input("To mark the task as complete press: 1\n"
                    +"To re assign the task to a differnt user press: 2\n"
                    +"To change the due date of a task press: 3\n"))

        # changeing a task to complete is done by 
        # isolating annd changing the relevant index
        if alteration == 1:
            task[5] = 'Yes'
            users_task_dict[x] = ", ".join(task)
            # this task is then added to the new file ready for printing
            new_task_file.append(users_task_dict[x])
            # an output message is sent to the return
            # to alert the user of success
            output = f'Task {x} has been marked complete.\n'

            '''changing the user is done the same as above by isolating the index
            and changing it to the new user
            however the username is checked against the users list for
            authenticity
            '''
        elif alteration == 2:
            # use a booleon to create loop for cross checking new user
            # against the user registered in user file
            update_incomplete = True
            # make a list with user info
            with open('user.txt' , 'r+') as users:
                for lines in users:
                    username_list.append(lines.split(',')[0])
            while update_incomplete:
                # request a username from user
                reassign_user = input(
                "Please enter a valid username to reassign this task to:\n")
                # check against the list
                # if the user exists change the index, else ask again
                if reassign_user in username_list:
                    task[0] = reassign_user
                    update_incomplete = False
                    users_task_dict[x] = ", ".join(task)
                    # send output to retunr to confirm success
                    output = (
                        f"Task {x} has been reassigned to {reassign_user}.\n")
                    # make sure info is added to new file for printing
                    new_task_file.append(users_task_dict[x])
                else:
                    print("User not found")

        # chnging the date is the same as above, isolate and change the 
        # relevant index 
        elif alteration == 3:
            new_due_date = input(
            f'Please enter the new due date for task {x}\n'
            +'Enter as: DD MON YYYY:\n')
            task[4] = new_due_date
            # make sure information is added to 
            # new_task_file data ready for printing
            users_task_dict[x] = ", ".join(task)
            new_task_file.append(users_task_dict[x])
            # send output to return confirming success
            output = (
                f'The due date for task {x}'
                +'has been changed to: {new_due_date}')

        else:
            output = '\n No changes were made\n'
    
    
    return print(output)

def task_overview():
    # local variables used inside this function
    content = ''
    task_count = 0
    incomplete_count = 0
    overdue_count = 0
    complete_tasks = 0
    overdue_incomplete_count = 0
    user_count = 0
    user_list = []
    task_list = []

    # iterate through the tasks file line by line and create
    # variable with all info
    tasks = open('tasks.txt', 'r')
    for lines in tasks:
        content += lines
    tasks.close()
    # turn the content into a list with each line as a index
    task_list = content.split('\n')
    # task amount is the number of index in list
    # one per task
    task_count = len(task_list)
    # iterate though the tasks list and collect infomation about each task
    for items in task_list:
        # split the task into a list in order to be abel to isolate indexs
        items = items.split(', ')
        print(items)
        print(items[5])
        # first using the 5th index, determin how many tasks ate incomplete
        if items[5] == 'No':
            incomplete_count += 1
            print(incomplete_count)
    # using the above gather in formation you can 
    # easily figure out how many tasks are complete.
    complete_tasks = task_count - incomplete_count
    # reapeat the above process to find the overdue tasks
    for items in task_list:
        info = items.split(', ')  # isolate indexs
        # reformat date at index 4
        date_on_file = datetime.strptime(info[4].replace(' ','/'), "%d/%b/%Y")
        # define date and time at time of review
        now = datetime.now()
        # if now is later than the the due date for the task
        #increase the overdue counter
        if now >= date_on_file:
            overdue_count += 1
        # same as above for overdue incomplete tasks
        # i feel like this is doubling down on info 
        # but the copy ask for it to be included so here it is
        if now >= date_on_file and info[5] == 'No':
            overdue_incomplete_count += 1
    # using information gathered above, percentages can be gerarated 
    # using variables with simple sums
    percentage_overdue = round((overdue_count / task_count) * 100,0)
    percentage_incompete = round((incomplete_count / task_count) * 100,0)

    # open (or create) a tasks_overview document and write the newly
    # accuired info in a legible way
    with open('tasks_overview.txt', 'w') as task_report:
        task_report.write(
            f'Total tasks:'
            +f'  {task_count}\n'
            f'Incomplete tasks:'
            +f' {incomplete_count}\n'
            f'Overdue tasks:'
            +f' {overdue_count}\n'
            f'Incomplete overdue tasks:'
            +f' {overdue_incomplete_count}\n'
            f'Percentage of tasks overdue:'
            +f' {percentage_overdue}%\n'
            f'Percentage of tasks incomplete:'
            +f' {percentage_incompete}%')
    #once written, close the document.
    task_report.close()
    # user reports
    # task_info_dict is used to collect the information for each user with 
    # users as the keys
    task_info_dict ={}
    # first thing to do is collect all the users from the user file
    # at the same time as collating the list also increase the 
    # total users_count for later inclusion
    users = open('user.txt', 'r')
    for lines in users:
        user_count += 1
        user_list.append(lines.split(', ')[0])
    # close the user doc
    users.close()

    # open a for loop to iterate through each user in the user list
    for users in user_list:
        # variables must be reset for each user at the top of the loop
        user = users
        users_tasks = 0
        task_complete = 0
        tasks_incomplete = 0
        tasks_overdue = 0
        total_task = 0
        # for each user, iterate though the tasks list (generated earlier)
        # and increase the counters for each true statement found
        for tasks in task_list:
            # tasks must be split into lists to isolate indexs
            task = tasks.split(', ')
            # task due date is reformatted ready for use
            task_due_date = datetime.strptime(task[4].replace(' ','/'), "%d/%b/%Y")
            # first counter for users total tasks
            if task[0] == user:
                users_tasks += 1
            # second counter for users complete tasks
            if task[0] == user and task[-1] == 'Yes':
                task_complete += 1
            # third counter for users incomplete tasks
            if task[0] == user and task[-1] == 'No':
                tasks_incomplete += 1
            # forth counter for overdue tasks using datetime library
            if task[0] == user and now >= task_due_date and task[-1] == "No":
                tasks_overdue += 1
            # total tasks for all users count
            # use to calculate percentages
            total_task += 1
        # counter results are then input into the task_info_dict for the
        # relevant user
        # order = user/ users total/ users complete/
        # users incomplete/ users overdue and incomplete/ workload%
        task_info_dict[user] = [
        users_tasks, task_complete, tasks_incomplete, 
        tasks_overdue, round(((users_tasks /total_task) * 100),0)]

    # the following technique for printing was learned at stackabuse.com
    # set the default print output as a variable
    original_stdout = sys.stdout
    # open the user overview file
    with open('user_overview.txt', 'w') as report:
        # change the print out location to this file
        sys.stdout = report
        # I adapted this following code
        #  from one of your examples codes for fun.
        # this first secction generates the print out for the criteria
        report_creiteria = [
        'User', 'Total', 'Complete', 'Incomplete', 'Overdue', 'Workload %']
        # each heading is spaces out on a single lines by a tab
        for i in range(len(report_creiteria)):
            print(report_creiteria[i], '\t', end=' ')
        print()
        # the information for each key (which hold each user)
        # is then printed with tab spaceing so that the relevant
        # info falls unser the relevant heading printed above
        keys = task_info_dict.keys()
        for x in keys:
            print(x, '\t', end=' ')
            report = task_info_dict[x]
            for i in range(len(report)):
                print(report[i], '\t','\t', end= ' ')
            print()
        # some final overview statisitaics are printed below
        print(f'Total Users: {user_count}')
        print(f'Total Tasks: {task_count}')
        # retunr the print location back to the console
        sys.stdout = original_stdout
    # report confirmation to the user with the retun function
    return(print(
        "\n - Reports have been generated and sent to program files - \n"))


def statistics():
    # check to see if the file exists in folder
    # and if it doesnt use the task overiew function to generate reports
    if os.path.exists('tasks_overview.txt') == False:
        task_overview()
    ''' when the appropriate file is in place:
    open the file, extract the info and print to screen line by line
    the info should already be well formatted.
    '''
    with open('tasks_overview.txt', 'r') as report:
        print("\n - The current macro statistics are as follows. -\n")
        for lines in report:
            print(lines)
        print()

    # this function checks for the other file even though the
    # files are typically generated together
    # this is a precausion incase one has been deleted accidentally
    if os.path.exists('user_overview.txt') == False:
        task_overview()
    # same as above for second file
    with open('user_overview.txt', 'r') as report:
        print("\n - The statistics on a per user basis are as follows. -\n")
        for lines in report:
            print(lines)




#=========Login Section================================
username_required = True
password_required = True
# open a loop for authenticating the username using username_required booleon
while username_required:
    with open('user.txt', 'r') as users:
        username = input("Please enter a valid username:\n")
        for lines in users:
            # I chose not to use a list here because I dont want
            # to create a passwords list aswell and store it
            # inside the active program. i just want to take
            # the password that is needed.
            # if a match is found
            if username in lines:
                    print('User confirmed')
                    username_required = False
                    # once a valid username is entered
                    # a username is no longer required
                    # the password for this user will always be 
                    # the next word on the same line.
                    # save the password using a split and an integer selection
                    true_password = [lines.split()[1]]
# once the username loop is closed a password is requested
# entered password must match true_password exactly
# start a loop for password authentiacation
while password_required:
    password = input("Please enter your password:\n")
    if password in true_password:  # if the password matches true_password
        print("\n- Login Successful. -")
        # once the correct password is entered 
        # password_required becomes false and closes the loop
        # login success becomes true
        password_required = False
        login_success = True
    # or else keep asking for password
    else:
        print("Password is incorrect, Please try again.")


#==========main menu==============
while login_success:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    # a specific menu applys only to username "admin"
    if username == "admin":
        menu = input('''
    Select one of the following Options below by typing the corresponding letter:

    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    s - Statistics
    ta - Task overview
    e - Exit

    Type Selection here: ''').lower()  # admin only menu

    else:
        menu = input('''
    Select one of the following Options below by typing the corresponding letter:

    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit

    Type Selection here: ''').lower()  # normal user menu

    # =======response's to users selection=============
    # each selection will call the relevant function
    # apart from exit and loop back
    if menu == 'r' and username == "admin":  #admin specific content
            reg_user()
    elif menu == 'a':
            add_task()
    elif menu == 'va':
            view_all()
    elif menu == 'vm':
            view_my(username)
    elif menu == 's' and username == 'admin':  # admin specific content
            statistics()
    elif menu == 'ta':
        task_overview()

    elif menu == 'e':  # used to exit the program
        print('Goodbye!!!')
        exit()

    else:  # loop back to menu entry
        print("\n- You have made a wrong choice, Please Try again. -")



# Adapted from my original submission for the SE bootcamp - Oct-2022