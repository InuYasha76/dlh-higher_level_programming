#!/usr/bin/python3
"""This module is about serializing CSV to JSON"""


import csv
import json


def convert_csv_to_json(csv_file):
    """
    This function 
    Args:
        csv_file (string): The name of the CSV file to dump to data.json.
    Raises:
        Exception: such as FileNotFoundError.
    Returns:
        True if the convertion went well.
        False if there were errors.
"""
    try:
        data = []
        json_file = "data.json"
        # Opens the csv file in read mode
        # Instanciates a DictReader class reader object
        # DictReader converts each row of the csv file into a dictionary
        # Each resulting dictionary appends to a data list as per task 
        # Closes the file at then end of the with statement
        with open(csv_file, "r", encoding="utf-8") as csv_f:
            csv_reader = csv.DictReader(csv_f)
            for row in csv_reader:
                data.append(row)
        # Opens the data.json file in write mode:
        # - Creates the data.json file if non existent
        # - Overwrites the data.json file if existent
        # Dumps the list of dictionaries into the data.json file
        # Closes the json_file when written at the end of with statemtent
        with open(json_file, "w", encoding="utf-8") as json_f:
            json.dump(data, json_f)
        # Returns True as per task statement
        return True

    except FileNotFoundError:
        print("CSV file not found")
        return False
    except Exceptions as e:
        print(f"An error occurred: {e}")
        return False
