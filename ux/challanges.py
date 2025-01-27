import matplotlib.pyplot as plt

# Data for Challenges Faced
labels_challenges = ['Content difficulty', 'Practical use', 'Interface issues', 'Lesson quality']
sizes_challenges = [10, 8, 5, 7]
colors_challenges = ['#ff9999', '#ffcc99', '#66b3ff', '#99ff99']  # Colors indicating different types of challenges

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(labels_challenges, sizes_challenges, color=colors_challenges)
plt.title('Challenges Faced by Duolingo Users')
plt.xlabel('Type of Challenge')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=45)  # Rotate labels for better readability
plt.tight_layout()  # Adjust layout to make room for label rotation

# Show the plot (not displaying here, just use this line when running in your environment)
plt.show()
