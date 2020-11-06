import matplotlib.pyplot as plt

label = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl'
sizes = [33, 52, 12, 17, 62, 48]
separated = (1, 0, 0, 0, 0, 0)

plt.pie(sizes, labels=label, autopct='%1.1f%%', explode=separated)
plt.axis('equal')
plt.show()