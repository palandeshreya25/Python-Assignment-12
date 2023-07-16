from file_handling import *

def add_employee():
    employee_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    # Additional employee details can be added here
    employee_data = {
        "employee_id": employee_id,
        "name": name
    }
    write_data_to_file("employees.txt", employee_data)
    print("Employee added successfully.")

def update_employee():
    employee_id = input("Enter employee ID to update: ")
    employee_data = read_data_from_file("employees.txt")
    if employee_id in employee_data:
        new_name = input("Enter new name for the employee: ")
        employee_data[employee_id]["name"] = new_name
        write_data_to_file("employees.txt", employee_data)
        print("Employee details updated successfully.")
    else:
        print("Employee not found.")

def delete_employee():
    employee_id = input("Enter employee ID to delete: ")
    employee_data = read_data_from_file("employees.txt")
    if employee_id in employee_data:
        del employee_data[employee_id]
        write_data_to_file("employees.txt", employee_data)
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")