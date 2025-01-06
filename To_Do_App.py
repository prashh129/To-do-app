import json
tasks_file="tasks.json"

def load_task():
    try:
        with open(tasks_file,"r") as f:
            return json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        return []

def save_task():
    with open(tasks_file,"w") as f:
        json.dump(tasks,f)

tasks=load_task()

def show_menu():
    print("\nTo Do App")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Quit")

def add_task():
    task=input("\nEnter your task: ").strip()
    if task:
        tasks.append(task)
        save_task()
        print(f"\nTask added: {task}")
    else:
        print("\nTask can not be empty")

def view_task():
    if not tasks:
        print("No tasks found!!!")
    else:
        print("\n")
        for i,txt in enumerate(tasks,start=1):
            print(f"{i}.{txt}")

def del_task():
    view_task()
    task_num=int(input("\nEnter your task number you want to delete: "))
    try:
        if (1<task_num>len(tasks)):
            print("\nPlease enter valid task number!")
        else:
            removed_task=tasks.pop(task_num-1)
            save_task()
            print(f"\nTask deleted: {removed_task}")
    except:
        print("\nPlease check your input again!")



while True:
    show_menu()
    choice=int(input("Please enter your choice: "))
    if choice==1:
        add_task()
    elif choice==2:
        view_task()
    elif choice==3:
        del_task()
    elif choice==4:
        print("\nThank you for using my program!")
        break
    else:
        print("\nPlease choose between 1-4")
    







