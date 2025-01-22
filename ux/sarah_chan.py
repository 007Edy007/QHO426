import matplotlib.pyplot as plt

steps_sarah = ["Discovery (University Club)", "Sign-Up", "Initial Assessment", "Engagement", "Supplementary Learning", "Challenges"]
y_positions = range(len(steps_sarah))

plt.figure(figsize=(8, 5))
plt.plot(steps_sarah, y_positions, marker='^', linestyle='--', color='magenta', markersize=8, linewidth=2)
plt.yticks(y_positions, steps_sarah)
plt.gca().invert_yaxis()
plt.title("Sarah Chen's User Journey")
plt.grid(True)
plt.show()
