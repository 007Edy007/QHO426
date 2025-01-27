import matplotlib.pyplot as plt

# Data for Most Useful Feature
labels_features = ['Daily lessons', 'Language tips', 'Stories and podcasts', 'Progress quizzes']
sizes_features = [15, 5, 7, 3]
colors_features = ['#66b3ff', '#ffcc99', '#99ff99', '#ff9999']  # Assigning colors for better visual differentiation

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes_features, labels=labels_features, colors=colors_features, autopct='%1.1f%%', startangle=140)
plt.title('Most Useful Features in Duolingo')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the plot (not displaying here, just use this line when running in your environment)
plt.show()
