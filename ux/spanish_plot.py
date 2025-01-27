import matplotlib.pyplot as plt

# Data Setup for Spanish
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
spanish_learning_minutes = [15, 25, 0, 25, 35, 30, 20]  # Minutes spent learning Spanish each day

# Plotting Spanish Learning Time
plt.figure(figsize=(10, 6))
plt.bar(days, spanish_learning_minutes, color='lightblue')
plt.title('Learning Time Over the Last 7 Days - Spanish')
plt.xlabel('Day of the Week')
plt.ylabel('Learning Time (minutes)')
plt.ylim(0, 70)  # Set y-axis limits to give some space above the highest bar
plt.show()
