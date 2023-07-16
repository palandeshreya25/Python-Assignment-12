import json

def read_data_from_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}

def write_data_to_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)