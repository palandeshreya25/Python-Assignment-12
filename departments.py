from file_handling import *

def add_department():
    department_id = input("Enter department ID: ")
    name = input("Enter department name: ")
    # Additional department details can be added here
    department_data = {
        "department_id": department_id,
        "name": name
    }
    write_data_to_file("departments.txt", department_data)
    print("Department added successfully.")

def update_department():
    department_id = input("Enter department ID to update: ")
    department_data = read_data_from_file("departments.txt")
    if department_id in department_data:
        new_name = input("Enter new name for the department: ")
        department_data[department_id]["name"] = new_name
        write_data_to_file("departments.txt", department_data)
        print("Department details updated successfully.")
    else:
        print("Department not found.")

def delete_department():
    department_id = input("Enter department ID to delete: ")
    department_data = read_data_from_file("departments.txt")
    if department_id in department_data:
        del department_data[department_id]
        write_data_to_file("departments.txt", department_data)
        print("Department deleted successfully.")
    else:
        print("Department not found.")