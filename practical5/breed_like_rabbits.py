#Number of rabbits in the first generation with known conditions
#a is the number of the generation,b is the number of rabbit
#The while loop indicates the number of rabbits after each generation is increa$
#With each new generation, the rabbit population doubles
#Exit the loop when the number of rabbits is more than 100
#Output the generations of rabbits at this time
a=1
b=2
while 1==1:
 a+=1
 b=b*2 
 if b>100:
  print("The generation that over 100 rabbits have been born is",a)
  break
