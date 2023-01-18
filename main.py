import matplotlib.pyplot as plt
import numpy as np

#Creating simple arrays numpy array -1
#x=np.array([0,100]) #Creating array from 0 to 100. Arrays are similar to list
#y = np.array([0,4])

#Plotting x and y - a simple line
#The first argument is the x-axis and the second is the y-axis
#plt.plot(x,y)

#You always need to type plt.show() in order to see the graph.
#plt.show()

#Plotting several point in matplotlib -2
#The numpy arrays has to be the same lenght. Matplotlib pairs point in x and y.
#x=np.array([0,30,12,56,19,100]) 
#y = np.array([40,72,80,13,17,39])
#plt.plot(x,y)
#plt.show()

#x=np.array([0,10,20,30,40,100]) 
#y = np.array([0,1,2,3,4,30])
#plt.plot(x,y)
#plt.show()

#Instead of a line graph, we want a scatter graph
#Method one
#x=np.array([0,30,12,56,19,100]) 
#y = np.array([40,72,80,13,17,39])
#plt.plot(x,y,"o") #pass o as an argument
#plt.show()

#Method two
#x=np.array([0,30,12,56,19,100]) 
#y = np.array([40,72,80,13,17,39])
#plt.scatter(x,y) 
#plt.show()

#Matplotlib's default x and y axis
x=np.array([0,10,20,30,100]) 
plt.plot(x)
plt.show()
