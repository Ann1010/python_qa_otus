import json


def read_json(json_file_name):
    with open(json_file_name, 'r') as json_file:
        result = json.load(json_file)
    return result
