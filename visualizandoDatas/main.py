import matplotlib.pyplot as plt

year = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000,
         2005, 2010, 2015]

pop = [2.5, 2.7, 3.0,
         3.3, 3.6, 4.0, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]

death = [1.2, 1.7, 1.8, 2.2, 2.5, 2.7, 2.9, 3, 3.1, 3.3,
          3.5, 3.8, 4.0, 4.3]

#plt.plot(year, pop, "-", color=(255/255, 100/255, 100/255))
#plt.plot(year, death, color=(.6, .6, 1))
line = plt.plot(year, pop, year, death)
plt.grid(True)

plt.setp(line, color=(.4, .4, 1), marker=".")

plt.ylabel("Population in billions")
plt.xlabel("Population growth by year")
plt.title("Population Growth")
plt.show()

