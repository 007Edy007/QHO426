import matplotlib.pyplot as plt
import pandas as pd

# Data Setup
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
learning_minutes = [30, 45, 20, 50, 35, 60, 40]  # Minutes spent learning each day

# Create a DataFrame
df = pd.DataFrame({
    "Day": days,
    "Learning Time (min)": learning_minutes
})

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df["Day"], df["Learning Time (min)"], color='skyblue')
plt.title('Learning Time Over the Last 7 Days')
plt.xlabel('Day of the Week')
plt.ylabel('Learning Time (minutes)')
plt.ylim(0, 70)  # Set y-axis limits to give some space above the highest bar
plt.show()
