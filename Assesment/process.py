"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv

def load_dataset(filepath):
    """Loads the dataset from a CSV file."""
    data = []
    try:
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
    return data

def handle_view_data_choice(choice, data):
    """Handles user selection in the View Data sub-menu."""
    if choice == 'A':
        print("You selected: View Reviews by Park")
        print(f"Dataset contains {len(data)} rows. (This will be filtered by park in the future)")
    elif choice == 'B':
        print("You selected: Number of Reviews by Park and Reviewer Location")
        print(f"Dataset contains {len(data)} rows. (This will calculate counts by park and location in the future)")
    elif choice == 'C':
        print("You selected: Average Score per year by Park")
        print(f"Dataset contains {len(data)} rows. (This will calculate average scores per year in the future)")
    elif choice == 'D':
        print("You selected: Average Score per Park by Reviewer Location")
        print(f"Dataset contains {len(data)} rows. (This will calculate averages by park and location in the future)")
    else:
        print("Invalid choice. Returning to the View Data menu.")
