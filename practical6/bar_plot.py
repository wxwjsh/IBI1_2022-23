#The number of input samples is N
#Enter the number of each sample as the height of the bar chart
#Enter the width of the bar chart
#Import the statistical chart title, x axis and y axis
#Set the Y-axis to 0-40
import numpy as np
import matplotlib. pyplot as plt
N=8
costs=(1,8,15,7,5,14,43,40)
ind=np.arange(N)
width=0.55
p1= plt.bar(ind,costs,width,color=['r','y','c','g','b','m','k','crimson'])
plt. ylabel('Cost(in $ billions)')
plt.title('The cost of the Olympic Game')
plt.xticks(ind,('Los Angeles 1984','Seoul 1998','Barcelona 1992','Atlanta1996','Sydney 2000','Athens 2003','Beijing 2008','London 2012')) 
plt.yticks (np.arange(0, 41, 5))
plt. show()
