import matplotlib.pyplot as plt

# Data for Motivation for Using Duolingo
labels_motivation = ['Learning new language', 'Refreshing skills', 'Academic', 'Career']
sizes_motivation = [18, 4, 3, 5]
colors_motivation = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(labels_motivation, sizes_motivation, color=colors_motivation)
plt.title('Motivation for Using Duolingo')
plt.xlabel('Motivation')
plt.ylabel('Number of Respondents')
plt.show()
