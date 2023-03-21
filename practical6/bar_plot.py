import numpy as np
import matplotlib. pyplot as plt
N=8
scores=(1,8,15,7,5,14,43,40)
ind=np.arange(N)
width=0.35
p1= plt. bar(ind, scores, width)
plt. ylabel('Cost(in $ billions)')
plt.title('The cost of the Olympic Game')
plt.xticks(ind,('Los Angeles 1984','Seoul 1998','Barcelona 1992','Atlanta1996','Sydnet 2000','Athens 2003','Beijing 2008','London 2012')) 
plt.yticks (np.arange(0, 41, 5))
plt. show()
