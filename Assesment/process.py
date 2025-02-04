"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv

def load_dataset(filepath):
    data = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
    return data

def handle_view_data_choice(choice, data):
    if choice == 'X':
        return
    elif choice == 'A':
        park_name = input("Enter the park name to view its reviews: ")
        view_reviews_by_park(data, park_name)
    elif choice == 'B':
        park_name = input("Enter the park name: ")
        location = input("Enter the reviewer location: ")
        count_reviews_by_park_and_location(data, park_name, location)
    elif choice == 'C':
        park_name = input("Enter the park name: ")
        year = input("Enter the year (YYYY): ")
        average_rating_by_park_and_year(data, park_name, year)
    elif choice == 'D':
        park_name = input("Enter the park name: ")
        location = input("Enter the reviewer location: ")
        average_score_per_park_by_location(data, park_name, location)
    else:
        print("Invalid choice. Please try again.")

def view_reviews_by_park(data, park_name):
    filtered_reviews = [review for review in data if review['Branch'] == park_name]
    if not filtered_reviews:
        print("No reviews found for this park.")
    else:
        for review in filtered_reviews:
            print(f"Review ID: {review['Review_ID']}, Rating: {review['Rating']}, Year: {review['Year_Month']}, Reviewer: {review['Reviewer_Location']}")

def count_reviews_by_park_and_location(data, park_name, location):
    count = sum(1 for review in data if review['Branch'] == park_name and review['Reviewer_Location'] == location)
    print(f"Number of reviews for {park_name} from {location}: {count}")

def average_rating_by_park_and_year(data, park_name, year):
    ratings = [int(review['Rating']) for review in data if review['Branch'] == park_name and review['Year_Month'].startswith(year)]
    if not ratings:
        print("No ratings found for this park in the specified year.")
    else:
        average_rating = sum(ratings) / len(ratings)
        print(f"Average rating for {park_name} in {year}: {average_rating:.2f}")

def average_score_per_park_by_location(data, park_name, location):
    ratings = [int(review['Rating']) for review in data if review['Branch'] == park_name and review['Reviewer_Location'] == location]
    if not ratings:
        print("No reviews found for this park from this location.")
    else:
        average_rating = sum(ratings) / len(ratings)
        print(f"Average rating for {park_name} from {location}: {average_rating:.2f}")


