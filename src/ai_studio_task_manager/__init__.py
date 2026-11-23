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
def delete_task():
    view_tasks()
    task_number = int(input("Enter task number to delete: "))
    removed_task = tasks.pop(task_number - 1)
    print(f"Deleted task: {removed_task}")           

def main():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
         print("Exiting application. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
if __name__=="__main__":
    main()
