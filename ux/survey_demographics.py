import matplotlib.pyplot as plt

# Data for Survey Demographics
labels_demographics = ['Friends', 'Family', 'Colleagues', 'Acquaintances']
sizes_demographics = [10, 5, 10, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes_demographics, labels=labels_demographics, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Survey Demographics')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
