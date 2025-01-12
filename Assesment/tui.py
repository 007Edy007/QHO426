"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

def display_welcome():
    title = "Disneyland Review Analyser"
    dashes = "-" * len(title)
    print(dashes)
    print(title)
    print(dashes)
    print()

def display_main_menu():
    print("Please enter the letter which corresponds with your desired menu choice:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")
    return input("Enter your choice: ").strip().upper()

def display_invalid_choice():
    print("Invalid choice. Please try again.")

def display_view_data_menu():
    print("\nPlease enter one of the following options:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per year by Park")
    print("[D] Average Score per Park by Reviewer Location")
    print("[X] Exit") # added option to be able to return to the previous menu
    return input("Enter your choice: ").strip().upper()

def display_visualise_data_menu():
    print("\nPlease enter one of the following options:")
    print("[A] Most Reviewed Parks")
    print("[B] Average Scores")
    print("[C] Park Ranking by Nationality")
    print("[D] Most Popular Month by Park")
    print("[X] Exit") # added option to be able to return to the previous menu
    return input("Enter your choice: ").strip().upper()

def handle_view_data_choice(choice, data):
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



