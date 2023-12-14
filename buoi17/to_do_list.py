import json
def add_task():
    task_name = input("Input task name: ")
    task = {
        "task_name": task_name,
        "status": task_status[0],
    }
    task_list.append(task)

def display_task_list():
    for task in task_list:
        print(f'Task name: {task["task_name"]}')
        print(f'Task status: {task["status"]}')
        print('------------------')

def check_task():
    display_task_list()
    task_name = input("Input task name: ")
    for task in task_list:
        if (task["task_name"] == task_name):
            task["status"] = task_status[1]
    display_task_list()

def save_task_list():
    with open('todo_list.json', 'w') as file:
        json.dump(task_list, file)

def load_task_list():
    with open('todo_list.json', 'r') as file:
        return json.load(file)

running = True
print('--- To do app ---')
task_list = []
task_status = ('Pending', 'Done')
while running:
    print('''
          1/ Add task
          2/ Display task
          3/ Check task
          4/ Save task list
          5/ Load task list
          6/ Exit
    ''')
    select:int = int(input("Select function: "))
    if select == 1:
        add_task()        
        print("Successfully add task")
    elif select == 2:
        print('--- Task list ---')
        display_task_list()
    elif select == 3:
        check_task()
    elif select == 4:
        save_task_list()
    elif select == 5:
        task_list = load_task_list()
        display_task_list()
    elif (select == 6):
        running = False
