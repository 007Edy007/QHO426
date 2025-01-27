import matplotlib.pyplot as plt

# Data setup for User Engagement and Satisfaction
labels = ['Overall Satisfaction', 'Suggestions for Enhancement']
sizes = [90, 10]  # Percentage of users satisfied vs. those who suggested enhancements
colors = ['lightgreen', 'salmon']

# Create pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('User Engagement and Satisfaction')
plt.show()
