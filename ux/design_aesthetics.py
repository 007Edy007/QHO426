import matplotlib.pyplot as plt

# Data setup for Design and Aesthetics feedback
labels = ['Positive Feedback', 'Suggestions for Improvement']
sizes = [80, 70]  # Percentage of users (Note: These don't add up to 100 because they represent independent questions)
colors = ['lightblue', 'lightcoral']

# Create pie chart
plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Design and Aesthetics Feedback')
plt.show()
