# task_manager
A task management system created in python using CSV type data files.
# task_manager
## Basic task manager program designed in python using CSV files as databases.

To run this file in Docker play ground open an instance and type:
  docker run -i admbjmn/task_manager
 The files is easier to interpret in VS code and will provide you with more functionality - ie: viewing generated files. 
 
This Task Management system is a simple stand alone program that allows a user to read, update and delete entries in a file containing details about tasks.
There is also some basic functionality to generate reports and present data to the user in the console.

## __Key Components__

__Functions__
1. Reg User
2. add Task
3. View All
4. View My 
5. Task Alterations
6. Task Overview
7. Statistics

## Functions explained.

The Program starts with a Login function that refereences users and passwords from a separate textfile.
The program can be accessed by default with 
_username_: admin
_password_: adm1n
 
### Reg User
reg user allows users to add new users to the program so that they may have tasks associated to them.
The logged in user is poromted to enter a new username and password for the new user.
The password must be confirmed before the user can be succesfully added.
Once a Valid username and password has been entered the information is then added to the user.txt.


### Add Task
Add task allows the user to add tasks to the tasks.txt. The user is asked to input the relevant information for the new task
the tasks is then added to the task.txt file.


### View All
View all reads all tasks from the tasks.txt file and presents the information to the user 
in a useful manner. The user is then asked if any alterations are to be made to any tasks.
If so the task alteration function is called.


### View my
View my gathers information form the tasks file and any tasks associtated to the currently logged in user are presented in the console.


### Task Alterations
task alterations asks the user to indicate which change they would like to make
to mark as complete
to reassign the task
to change the due date
based on the response the program then gathers the needed information and updates the tasks.txt file.


### Task overview
Task overview creates two reports for use in the statistics function
the first report - task_overview.txt - contains macro information about the tasks on file.
information includes:
total tasks count
incomplete task count
percentage incomplete
overdue tasks
percentage overdue

The user report creates a files with task information on a user basis and saves the file as user_overiview.txt

### Statistics
statistics allows the user to get the information for the user_overview and the task_overview files and presents
them in the console in a useful way.
If the documents required arn't in the file then the task overview function is called to generate the files before the function continues.


## Basic Program flow.

Once logged in the user is presented with a main menu as follows:
![main menu](/images/main_menu.png)


By selecting one on the commands as instructed the user is then prompted with new istructions based on the selection.
EG:

![task_alterations](/images/task_alterations.png)


By continuing to follow the prompts on screen tasks can be taken care of and the CSV file will be updated.
Any functions that do not need user input will be displayed on screen and the menu will be re shown for 
any further requests.
EG:

![statistics](/images/statistics.png)


Once the user has finished the program can be closed from the main menu by typing exit.

_This program was made by adm.bjmn.
