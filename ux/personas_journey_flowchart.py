import matplotlib.pyplot as plt

journeys = {
    "Alex Johnson": ["Discovery (LinkedIn Ad)", "Sign-Up", "Initial Assessment", "Daily Learning", "Progress Tracking", "Challenges"],
    "Sarah Chen": ["Discovery (University Club)", "Sign-Up", "Initial Assessment", "Engagement", "Supplementary Learning", "Challenges"],
    "John Smith": ["Discovery (Online Search)", "Sign-Up", "Ease of Use", "Routine Learning", "Community Interaction", "Challenges"],
    "Emily Rivera": ["Discovery (Conference)", "Sign-Up", "Classroom Integration", "Feedback Implementation", "Advanced Features", "Challenges"]
}

fig, axs = plt.subplots(len(journeys), 1, figsize=(10, 20))  # Adjust the fig size based on your content
for ax, (persona, steps) in zip(axs, journeys.items()):
    ax.plot(steps, range(len(steps)), marker='o')  # Plotting the journey as points connected by lines
    ax.set_yticks(range(len(steps)))
    ax.set_yticklabels(steps)
    ax.invert_yaxis()  # Start the journey from the top
    ax.set_title(f"User Journey: {persona}")
    ax.grid(True)
fig.tight_layout()
plt.show()
