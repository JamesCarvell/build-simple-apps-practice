# written by James Carvell in python 3.6
# to be run from a terminal
# this todo list creates a text file to store a new list if one isn't found or
# the user wants to start over while running user can add tasks to list, or
# flag tasks as complete, call a help function for instructions, or exit


# add to list function
def add_to_list(new_task):


# check off function
def check_off(task_number):


# help function
help_text = """
Type 'help' and hit enter for function details. If the script is waiting for you
to add a new task, or check an task off, other functions won't work.
"""

def help():
    print("""
Type 'add' and hit enter to add a new task to the list, then type out the new
task and hit enter. Tasks are automatically numbered by order created. Writing
shorter tasks will be more legible later.

Type 'check' and hit enter, then type an task number and hit enter, to check
that task off on the list. It will still be there, just flagged as 'checked off'

Type 'done' and hit enter once you're done with the list. You can access it
again if you rerun the script and don't start a new list.
""" + "\b" +  help_text)

# checking for list text file, if none create new


# asking if user wants to start a new list if one already existed


# run while done = False print the list & help function instructions, wait
# for a function to be called, repeat
done = False
while done == False
    print("list placeholder")
    print(help_text)
    do_what = input(">")

    if do_what == "add"
        add_to_list(input(">"))

    if do_what == "check"
        check_off(input(">"))

    if do_what == "help"
        help()
