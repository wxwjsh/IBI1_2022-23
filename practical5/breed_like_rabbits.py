#Number of rabbits in the first generation with known conditions
a=1
b=2
#The while loop indicates the number of rabbits after each generation is increased
while 1==1:
 a+=1
 b=b*2
#Exit the loop when the number of rabbits is more than 100 
 if b>100:
#Output the generations of rabbits at this time  
  print("The generation that over 100 rabbits have been born is",a)
  break
