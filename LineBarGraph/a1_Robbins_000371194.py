""" 
a1_Robbins_000371194.py
I, Jacob Robbins, student number 000371194, certify that this material is my original work.
No other person's work has been used withoutdue acknowledgment and I have not made my work
available to anyone else.
"""

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(10)

#Data provided randomly generated

'''gen_normal function to create a randomly distributed list of floats
takes in mean and sd as its parameters, users can enter their desired parameters 
as need be
'''
def gen_normal(mean, sd):
    assert sd > 0, "Standard Deviation must be > 0"
    dat = np.random.normal(mean, sd, 20)
    return [mean, sd, dat]

#Two sets of data required, 30,5 & 10,4
data_standard_two = gen_normal(10,4)
data_standard = gen_normal(30,5)

'''
Two subsets of data required to create the lines that are plotted 
against the bar and line graphs
'''
data_set= [30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]
data_set_two= [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

#Define the figure size (image) of the output
plt.figure(figsize=(10,8))

#Blue Line Graph 
ax = plt.subplot(2,2,1)

plt.plot(data_standard[2],color='teal', linestyle='dotted')
plt.plot(data_standard_two[2],color='blue', linestyle="dashed")

plt.title('Normal Distributions (Line Graph)')
plt.xlabel('Array Index')
plt.ylabel('Random Value')
plt.legend(["mean=30, sd=5","mean=10, sd=4"],loc=1)

plt.plot(data_set, color='teal', linestyle="solid")
plt.plot(data_set_two, color='blue', linestyle="solid")
plt.axis([0,20,0,55])
ax.set_xticks([0,2,4,6,8,10,12,14,16,18,20])
ax.set_yticks([5,10,15,20,25,30,35,40,45,50,55])

#Yellow Line Graph 
ax1 = plt.subplot(2,2,2)

plt.plot(data_standard[2],color='#c4c31d',linestyle="solid",linewidth=4)
plt.plot(data_standard_two[2],color='green', linestyle='solid',linewidth=4)

plt.plot(data_set, color='#c4c31d', linestyle="dashed", gapcolor="white")
plt.plot(data_set_two, color='green', linestyle="dashed", gapcolor="white")

plt.legend(["mean=30, sd=5","mean=10, sd=4"],loc=1)
plt.title('Normal Distributions (Line Graph)')
plt.xlabel('Array Index')
plt.ylabel('Random Value')
plt.axis([0,20,0,55])
ax1.set_xticks([0,2,4,6,8,10,12,14,16,18,20])
ax1.set_yticks([5,10,15,20,25,30,35,40,45,50,55])

#Blue Bar Graph
ax2 = plt.subplot(2,2,3)
'''
Formula & variables used to adjust the plotting of the 
side-by-side bar graph follow they recur throughout the program
t*element + w*n for element in range(d)
'''
n = 1 # The first dataset
t = 1 # No of datasets
d = 20 # No of sets of bars
w = 0.8 # Width of each bar
data_standard_x = [t*element + w*n for element in range(d)]

#Plot the first set of data using aformentioned formula
plt.bar(data_standard_x, data_standard[2], color="teal", width=0.6)

n = 2  #The second dataset
t = 1 # Number of datasets
d = 20 # Number of sets of bars
w = 0.1 # Width of each bar
data_standard_two_x = [t*element + w*n for element in range(d)]

#Plot the first set of data using aformentioned formula
plt.bar(data_standard_two_x, data_standard_two[2], color="blue", width=0.6)

'''
Plotting legend title, x and y label structure found in 
following bar graph as well 
'''
plt.legend(["mean=30, sd=5","mean=10, sd=4"],loc=1)
plt.title('Normal Distributions (Bar Graph)')
plt.xlabel('Array Index')
plt.ylabel('Random Value')

#Plot the first set of data using aformentioned formula
plt.plot(data_set_two, color='blue', linestyle="dashed", gapcolor="white", linewidth=2)
plt.plot(data_set, color='teal', linestyle="dashed", gapcolor="white", linewidth=2)

#Define the axis, so that x and y meet at the 0 index
plt.axis([0,20,0,55])

#Plot the x ticks to adjust the frequency
ax2.set_xticks([0,2,4,6,8,10,12,14,16,18,20])
ax2.set_yticks([5,10,15,20,25,30,35,40,45,50,55])

#Yellow Bar Graph 
ax3 = plt.subplot(2,2,4)

n = 1 # The first dataset
t = 1 # N0 of datasets
d = len(data_standard[2]) # No of sets of bars
w = 0.2 # Width of each bar
data_standard_x = [t*element + w*n for element in range(20)]
plt.bar(data_standard_x, data_standard[2], color="#c4c31d")

data_standard_two_x = [t*element + w*n for element in range(d)]

plt.bar(data_standard_two_x, data_standard_two[2], color="green", width=0.5)

plt.legend(["mean=30, sd=5","mean=10, sd=4"],loc=1)
plt.title('Normal Distributions (Bar Graph)')
plt.xlabel('Array Index')
plt.ylabel('Random Value')
plt.plot(data_set, color='#c4c31d', linestyle="solid")
plt.plot(data_set_two, color='green', linestyle="solid")
plt.axis([0,20,0,55])
ax3.set_xticks([0,2,4,6,8,10,12,14,16,18,20])
ax3.set_yticks([5,10,15,20,25,30,35,40,45,50,55])


plt.subplots_adjust(wspace=0.35)
plt.subplots_adjust(hspace=0.5)

plt.show()