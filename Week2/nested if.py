# Ask the user for the cover type of the book
print ("Enter the cover type of the book (hard or soft): ")
cover_type = input()
# Check if the cover type is "soft"
if cover_type == "soft":
    # Ask if the book is perfect bound
    print ("Is the book perfect bound? (yes or no): ")
    perfect_bound = input()
    # Display the appropriate message based on the user's response
    if perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
# Check if the cover type is "hard"
elif cover_type == "hard":
    print("Books with hard covers can be more expensive!")
# Handle invalid input for cover type
else:
    print("Invalid cover type entered. Please enter either 'hard' or 'soft'.")