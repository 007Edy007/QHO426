import matplotlib.pyplot as plt

# Data for Usage Frequency
labels_usage = ['Daily', 'Several times a week', 'Weekly', 'Rarely']
sizes_usage = [12, 10, 6, 2]
colors_usage = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99']

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(labels_usage, sizes_usage, color=colors_usage)
plt.title('Usage Frequency')
plt.xlabel('Frequency')
plt.ylabel('Number of Respondents')
plt.show()
