"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
from visual import handle_visualise_data_choice
from process import load_dataset, handle_view_data_choice
from tui import (
display_welcome,
display_main_menu,
display_invalid_choice,
display_view_data_menu,
display_visualise_data_menu,
)

def main():

    print("Loading dataset...")
    data = load_dataset("disneyland_reviews.csv")
    if not data:
        print("Failed to load dataset. Exiting program.")
        return
    print(f"Dataset loaded successfully. Total rows: {len(data)}")
    print(f"DEBUG: Loaded data contains {len(data)} rows.")

    display_welcome() #modified version to get the title on top

while True:
    choice = display_main_menu()
    if choice == 'X':
        print("Exiting the program. Goodbye!")
        break
    elif choice == 'A':
        print("You selected: View Data")
        while True:
            sub_choice = display_view_data_menu()
            if sub_choice == 'x':
                break
            handle_view_data_choice(sub_choice, data)
    elif choice == 'B':
        print("You selected: Visualise Data")
        while True:
            sub_choice = display_visualise_data_menu()
            if sub_choice == 'x':
                break
            handle_visualise_data_choice(sub_choice, data)

    else:
        display_invalid_choice()

if __name__ == "__main__":
    main()


