"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import matplotlib.pyplot as plt


def handle_visualise_data_choice(choice, data):
    if choice == 'X':
        return
    elif choice == 'A':
        plot_most_reviewed_parks(data)
    elif choice == 'B':
        plot_average_scores(data)
    elif choice == 'C':
        park_name = input("Enter the park name to show top 10 reviewer locations: ")
        plot_top_locations_by_ratings(data, park_name)
    elif choice == 'D':
        park_name = input("Enter the park name to show average monthly ratings: ")
        plot_average_monthly_ratings(data, park_name)
    else:
        print("Invalid choice. Please try again.")


def plot_most_reviewed_parks(data):
    park_counts = {}
    for review in data:
        park = review['Branch']
        if park in park_counts:
            park_counts[park] += 1
        else:
            park_counts[park] = 1

    parks = list(park_counts.keys())
    counts = list(park_counts.values())

    plt.figure(figsize=(10, 8))
    plt.pie(counts, labels=parks, autopct='%1.1f%%', startangle=90)
    plt.title('Number of Reviews per Park')
    plt.axis('equal')
    plt.show()

def plot_average_scores(data):
    scores = {}
    counts = {}
    for review in data:
        park = review['Branch']
        rating = int(review['Rating'])
        if park in scores:
            scores[park] += rating
            counts[park] += 1
        else:
            scores[park] = rating
            counts[park] = 1

    averages = {park: scores[park] / counts[park] for park in scores}

    parks = list(averages.keys())
    avg_scores = list(averages.values())

    plt.figure(figsize=(12, 6))
    plt.bar(parks, avg_scores, color='green')
    plt.xlabel('Parks')
    plt.ylabel('Average Rating')
    plt.title('Average Review Scores by Park')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_top_locations_by_ratings(data, park_name):
    location_ratings = {}
    for review in data:
        if review['Branch'] == park_name:
            location = review['Reviewer_Location']
            rating = int(review['Rating'])
            if location in location_ratings:
                location_ratings[location].append(rating)
            else:
                location_ratings[location] = [rating]

    location_averages = {location: sum(ratings) / len(ratings) for location, ratings in location_ratings.items()}
    location_averages_sorted = sorted(location_averages.items(), key=lambda x: x[1], reverse=True)[:10]
    locations, averages = zip(*location_averages_sorted) if location_averages_sorted else ([], [])

    plt.figure(figsize=(12, 6))
    plt.bar(locations, averages, color='purple')
    plt.xlabel('Locations')
    plt.ylabel('Average Rating')
    plt.title(f'Top 10 Locations by Average Rating for {park_name}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_average_monthly_ratings(data, park_name):
    monthly_ratings = {}
    month_order = {'1': 'Jan', '01': 'Jan', '2': 'Feb', '02': 'Feb', '3': 'Mar', '03': 'Mar',
                   '4': 'Apr', '04': 'Apr', '5': 'May', '05': 'May', '6': 'Jun', '06': 'Jun',
                   '7': 'Jul', '07': 'Jul', '8': 'Aug', '08': 'Aug', '9': 'Sep', '09': 'Sep',
                   '10': 'Oct', '11': 'Nov', '12': 'Dec'}

    for review in data:
        if review['Branch'] == park_name:
            year_month = review['Year_Month']
            if '-' in year_month:
                year, month = year_month.split('-')
                month_name = month_order.get(month.strip())
                if month_name:
                    rating = int(review['Rating'])
                    if month_name in monthly_ratings:
                        monthly_ratings[month_name].append(rating)
                    else:
                        monthly_ratings[month_name] = [rating]
                else:
                    print(f"Skipping invalid month data: {month}")
            else:
                print(f"Skipping entry with invalid Year_Month format: {year_month}")

    if monthly_ratings:
        monthly_averages = {month: sum(ratings) / len(ratings) for month, ratings in monthly_ratings.items()}
        months_sorted = sorted(monthly_averages.items(), key=lambda x: list(month_order.values()).index(x[0]))
        months, averages = zip(*months_sorted) if months_sorted else ([], [])

        plt.figure(figsize=(12, 6))
        plt.bar(months, averages, color='blue')
        plt.xlabel('Month')
        plt.ylabel('Average Rating')
        plt.title(f'Average Monthly Ratings for {park_name}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("No valid monthly data available to plot.")


