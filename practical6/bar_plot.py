#The number of input samples is N
#Enter the number of each sample as the height of the bar chart
#Enter the width of the bar chart
#Import the statistical chart title, x axis and y axis
#Set the Y-axis to 0-40
cities=['Los Angeles 1984','Seoul 1988','Barcelona 1992','Atlanta 1996','Sydney 2000','Athens 2003','Beijing 2008','London 2012']
costs=(1,8,15,7,5,14,43,40)
#arrange in order
sorted_values=sorted(costs)
print (sorted_values)
#find from the internet
#Redefining cities and spending in ascending order
import numpy
cities=numpy.array(cities)
costs=numpy.array(costs)
sortedcosts=costs.argsort()
sorted_cities=cities[sortedcosts]
sorted_costs=costs[sortedcosts]
import numpy as np
import matplotlib. pyplot as plt
width=0.55
p1= plt.bar(sorted_cities,sorted_costs,width,color=['r','y','c','g','b','m','k','crimson'])
plt. ylabel('Cost(in $ billions)')
plt.title('The cost of the Olympic Game')
#plt.xticks(cities)
plt.xlabel('cities')
plt.yticks (np.arange(0, 41, 5))
plt. show()
