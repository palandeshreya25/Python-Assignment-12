from employees import *
from departments import *
from tasks import *

def main_menu():
    print("Welcome to the Management System!")
    print("1. Employee Management")
    print("2. Department Management")
    print("3. Task Management")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        employee_management_menu()
    elif choice == "2":
        department_management_menu()
    elif choice == "3":
        task_management_menu()
    elif choice == "4":
        print("Exiting the Management System...")
        return
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def employee_management_menu():
    print("Employee Management Menu")
    print("1. Add Employee")
    print("2. Update Employee Details")
    print("3. Delete Employee")
    print("4. Back to Main Menu")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        update_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        employee_management_menu()

def department_management_menu():
    print("Department Management Menu")
    print("1. Add Department")
    print("2. Update Department Details")
    print("3. Delete Department")
    print("4. Back to Main Menu")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_department()
    elif choice == "2":
        update_department()
    elif choice == "3":
        delete_department()
    elif choice == "4":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        department_management_menu()

def task_management_menu():
    print("Task Management Menu")
    print("1. Assign Task to Employee")
    print("2. Update Task Status")
    print("3. View Task Details")
    print("4. Back to Main Menu")
    choice = input("Enter your choice: ")

    if choice == "1":
        assign_task()
    elif choice == "2":
        update_task_status()
    elif choice == "3":
        view_task_details()
    elif choice == "4":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        task_management_menu()

if __name__ == "__main__":
    main_menu()