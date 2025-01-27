import matplotlib.pyplot as plt

# Data Setup for French
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
french_learning_minutes = [15, 20, 20, 25, 0, 30, 20]  # Minutes spent learning French each day

# Plotting French Learning Time
plt.figure(figsize=(10, 6))
plt.bar(days, french_learning_minutes, color='lightgreen')
plt.title('Learning Time Over the Last 7 Days - French')
plt.xlabel('Day of the Week')
plt.ylabel('Learning Time (minutes)')
plt.ylim(0, 70)  # Set y-axis limits to give some space above the highest bar
plt.show()
