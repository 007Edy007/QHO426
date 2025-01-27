import matplotlib.pyplot as plt

# Data for Satisfaction with Learning Content
labels_satisfaction = ['Very satisfied', 'Satisfied', 'Neutral', 'Unsatisfied', 'Very unsatisfied']
sizes_satisfaction = [6, 12, 8, 3, 1]
colors_satisfaction = ['#66b3ff', '#99ff99', '#ffff99', '#ffcc99', '#ff9999']  # Colors from more positive to more negative

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(labels_satisfaction, sizes_satisfaction, color=colors_satisfaction)
plt.title('Satisfaction with Learning Content')
plt.xlabel('Level of Satisfaction')
plt.ylabel('Number of Respondents')
plt.show()
