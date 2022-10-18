# written by James Carvell in python 3.6
# to be run from a terminal; saves todo list as text file at location where
# script is run

# add to list function
def add_to_list(task):
    global todo_list
    todo_list.append("[ ] " + task + "\n")

# check off function
def check_off_task(task_number):
    global todo_list
    task = todo_list[task_number - 1]
    task = task[:1] + "X" + task[2:]
    todo_list[task_number - 1] = task

# read todo list funciton
def read_list():
    n = 1
    for task in todo_list:
        print(str(n) + ") " + task)
        n += 1

# erase todo list function
def erase_list():
    global todo_list
    todo_list = []
    print("new list started")

# help text
help_short = """
Type 'help' and hit enter for function details. If the script is waiting for you
to add a new task, or check an task off, other functions won't work.
"""

help_long = """
Type 'add' and hit enter to add a new task to the list, then type out the new
task and hit enter. Tasks are automatically numbered by order created. Writing
shorter tasks will be more legible later.

Type 'check' and hit enter, then type an task number and hit enter, to check
that task off on the list. It will still be there, just flagged as 'checked off'.

Type 'todo' to see your current todo list.

Type 'erase' to clear the current list.

Type 'done' and hit enter once you're done with the list. You can access it
again if you rerun the script and don't start a new list.
"""

# try to retrieve file contents and create list
try:
    file = open("todo_list.txt", "r")
    todo_list = file.readlines()
    file.close()
    print("existing list found")
except:
    erase_list()

# run while not done: take user input to determine which function to run next
done = False
while not done:
    print(help_short)
    do_what = input(">")

    if do_what == "add":
        add_to_list(input("task>"))
    elif do_what == "check":
        check_off_task(int(input("task #>")))
    elif do_what == "todo":
        read_list()
    elif do_what == "erase":
        erase_list()
    elif do_what == "help":
        print(help_long + "\b" + help_short)
    elif do_what == "done":
        done = True
    else:
        print("Not sure what you want")

file = open("todo_list.txt", "w")
file.writelines(todo_list)
file.close()
