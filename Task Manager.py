def task():
    return []  # Return an empty list

print("___Welcome To The Task Management App___")

tasks = []  # Define tasks list globally

total_task = int(input("Enter how many tasks you want to add: "))
for i in range(1, total_task + 1):
    task_name = input(f"Enter task {i}: ")
    tasks.append(task_name)

print(f"Today's tasks are:\n{tasks}")

while True:
    operation = int(input("Enter operation:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n"))

    if operation == 1:
        add = input("Enter task you want to add: ")
        tasks.append(add)
        print(f"Task '{add}' has been successfully added.")

    elif operation == 2:
        updated_val = input("Enter the task name you want to update: ")
        if updated_val in tasks:
            new_task = input("Enter the new task: ")
            index = tasks.index(updated_val)
            tasks[index] = new_task
            print(f"Task '{updated_val}' updated to '{new_task}'.")
        else:
            print(f"Task '{updated_val}' not found.")

    elif operation == 3:
        delete_val = input("Enter the task name you want to delete: ")
        if delete_val in tasks:
            tasks.remove(delete_val)
            print(f"Task '{delete_val}' has been deleted.")
        else:
            print(f"Task '{delete_val}' not found.")

    elif operation == 4:
        print(f"Current tasks are: {tasks}")

    elif operation == 5:
        break

    else:
        print("Invalid input. Please enter a number between 1 and 5.")

print("Thank you for using the Task Management App.")
