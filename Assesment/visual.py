"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

def handle_visualise_data_choice(choice, data):
    if choice == 'A':
        print("You selected: Most Reviewed Parks")
        print(f"Dataset contains {len(data)} rows.")
    elif choice == 'B':
        print("You selected: Average Scores")
        print(f"Dataset contains {len(data)} rows.")
    elif choice == 'C':
        print("You selected: Park Ranking by Nationality")
        print(f"Dataset contains {len(data)} rows.")
    elif choice == 'D':
        print("You selected: Most Popular Month by Park")
        print(f"Dataset contains {len(data)} rows.")
    else:
        print("Invalid choice. Returning to the Visualize Data menu.")


