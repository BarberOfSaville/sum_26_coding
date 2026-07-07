#Brian Saville
#June 23, 2026
#starting work on the data visualization project

import matplotlib
import matplotlib.pyplot as plt

#plotting a sample line graph
squares = [1, 4, 9, 16, 25, 36, 49]
plt.plot(squares)
plt.show()

#that was basic.
#next, making customizations to improve readability
squares = [1, 4, 9, 16, 25, 36, 49]
plt.plot(squares, linewidth = 5)

#setting chart title and label axes
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

plt.show()

#correcting the plot: give both input and output values
input_values = [1, 2, 3, 4, 5, 6, 7]
squares = [1, 4, 9, 16, 25, 36, 49]
plt.plot(input_values, squares, linewidth = 5)
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)
plt.show()


#plotting and styling individual points with scatter()
#scatter- plots a single point
plt.scatter(2,4, s = 200)

#set chart and label axes
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)
plt.show()


#You can use scatter to plot a series of points
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s = 100)
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)
plt.show()


#Calculating data automatically
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40)

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

#Set the range for each axis with axis()
plt.axis([0, 1100, 0, 1100000])
plt.show()