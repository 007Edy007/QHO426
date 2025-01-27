import matplotlib.pyplot as plt
import numpy as np

# Data setup
metrics = ['Points Earned', 'Time Spent (min)', 'Lessons Completed', 'Streaks (days)']
user_data = [1200, 310, 25, 30]
friends_data = [
    [1300, 300, 27, 28],  # Friend 1
    [1100, 350, 20, 25],  # Friend 2
    [1250, 320, 30, 32],  # Friend 3
    [1180, 305, 22, 29]   # Friend 4
]
friends_labels = ['Friend 1', 'Friend 2', 'Friend 3', 'Friend 4']
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon']

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))  # Adjust subplot layout for better visual distribution
axs = axs.ravel()  # Flatten the array for easier iteration

for i, ax in enumerate(axs):
    index = np.arange(len(metrics))
    bar_width = 0.35

    # Plotting data for user and one friend
    ax.bar(index, user_data, bar_width, label='User', color='navy')
    ax.bar(index + bar_width, friends_data[i], bar_width, label=friends_labels[i], color=colors[i])

    # Adding titles and labels
    ax.set_xlabel('Metrics')
    ax.set_ylabel('Values')
    ax.set_title(f'Comparison with {friends_labels[i]}')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(metrics)
    ax.legend()

plt.tight_layout()
plt.show()
