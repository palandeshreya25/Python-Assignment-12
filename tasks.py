from file_handling import *

def assign_task():
    employee_id = input("Enter employee ID to assign task: ")
    task = input("Enter task details: ")
    tasks_data = read_data_from_file("tasks.txt")
    if employee_id in tasks_data:
        tasks_data[employee_id].append(task)
    else:
        tasks_data[employee_id] = [task]
    write_data_to_file("tasks.txt", tasks_data)
    print("Task assigned successfully.")

def update_task_status():
    employee_id = input("Enter employee ID to update task status: ")
    tasks_data = read_data_from_file("tasks.txt")
    if employee_id in tasks_data:
        employee_tasks = tasks_data[employee_id]
        if len(employee_tasks) > 0:
            for i, task in enumerate(employee_tasks):
                print(f"{i+1}. {task}")
            task_index = int(input("Enter task index to update status: ")) - 1
            if task_index >= 0 and task_index < len(employee_tasks):
                new_status = input("Enter new status for the task: ")
                employee_tasks[task_index] = new_status
                write_data_to_file("tasks.txt", tasks_data)
                print("Task status updated successfully.")
            else:
                print("Invalid task index.")
        else:
            print("No tasks found for the employee.")
    else:
        print("Employee not found.")

def view_task_details():
    employee_id = input("Enter employee ID to view task details: ")
    tasks_data = read_data_from_file("tasks.txt")
    if employee_id in tasks_data:
        employee_tasks = tasks_data[employee_id]
        if len(employee_tasks) > 0:
            print(f"Tasks for Employee ID: {employee_id}")
            for i, task in enumerate(employee_tasks):
                print(f"{i+1}. {task}")
        else:
            print("No tasks found for the employee.")
    else:
        print("Employee not found.")