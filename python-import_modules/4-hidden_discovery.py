#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get all names defined in the module
    names = dir(hidden_4)

    # Filter and sort names
    # We skip names starting with "__"
    filtered_names = [name for name in names if not name.startswith("__")]
    filtered_names.sort()

    # Print each name on a new line
    for name in filtered_names:
        print(name)
