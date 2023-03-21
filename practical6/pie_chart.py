#To make a pie chart, type key1-key10 as label
#Then enter value1-value10 as the size of the pie chart
#Enter the distance from the center of the pie block
#Adjust pie percentages, directions, and shadows before making sure the height and width are equal
#Get a pie chart
import matplotlib.pyplot as plt
labels='Comedy','Action','Romance','Fantasy','Science-fiction','Horror','Crime','Documentary','History','War'
sizes=[73,42,38,28,22,19,18,12,8,7]
explode=(0.03,0,0,0,0,0,0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=0)
plt.axis('equal')
plt.show()
