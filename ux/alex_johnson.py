import matplotlib.pyplot as plt

steps_alex = ["Discovery (LinkedIn Ad)", "Sign-Up", "Initial Assessment", "Daily Learning", "Progress Tracking", "Challenges"]
y_positions = range(len(steps_alex))

plt.figure(figsize=(8, 5))
plt.plot(steps_alex, y_positions, marker='s', linestyle='-', color='darkblue', markersize=8, linewidth=2)
plt.yticks(y_positions, steps_alex)
plt.gca().invert_yaxis()
plt.title("Alex Johnson's User Journey")
plt.grid(True)
plt.show()
