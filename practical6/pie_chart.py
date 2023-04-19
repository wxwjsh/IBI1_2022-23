#make a dictionary with 10 keys and 10 values
favor_movie={'Comedy' :73,'Action' :42,' Romance' :38,'Fantasy' :28,'Science-fiction':22,'Horro':19,'Crime':18,'Document':12,'History':8,'War':7}
print(favor_movie)
#When the corresponding key is entered, the value is matched
movie=input("input a movie:")
students=favor_movie.get(movie)
print(students)

#To make a pie chart, type key1-key10 as label
#Then enter value1-value10 as the size of the pie chart
#Enter the distance from the center of the pie block
#Adjust pie percentages, directions, and shadows before making sure the height and width are equal
#Get a pie chart
import matplotlib.pyplot as plt
labels='Comedy','Action','Romance','Fantasy','Science-fiction','Horror','Crime','Documentary','History','War'
sizes=[73,42,38,28,22,19,18,12,8,7]
explode=(0.05,0,0,0,0,0,0,0,0,0)
colors=['honeydew','mistyrose','lightyellow','lavender']
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=0,colors=colors)
plt.axis('equal')
plt.show()

#Create a new dictionary that arranges the contents of the original directory in descending order of value， printing the first movie type and the number of favorite students
#Code source network
best= sorted(favor_movie.items(),key=lambda x: x[1], reverse=True)
print('Their favorite movie and the number of students is : ',best[0])
