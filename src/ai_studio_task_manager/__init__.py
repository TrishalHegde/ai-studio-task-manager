tasks=[]
def add_task():
    task=input("Enter a task: ")
    tasks.append(task)
    print("Task added sucessfully ")
def view_tasks():
    print("Your task are :")
    if len(tasks)==0:
        print("No tasks available")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")
if __name__=="__main__":
    main()
