import matplotlib.pyplot as plt #Pyplot's a collection of function, each of which makes a change to a chart

input_values= range(1,1001)
squares = [number**2 for number in input_values]

plt.style.use("seaborn-dark")

fig, ax = plt.subplots()
'''The subplots() -functions returns a tuple of two objects. Fig is frame-object with which the frame of your chart can be f.ex. resized or reshaped.
Every frame can have mulitple axis to display your data.
Ax, short for axes, is the canvas on which your data is plotted. 
Axes-object can only belong to a single frame. More at https://towardsdatascience.com/clearing-the-confusion-once-and-for-all-fig-ax-plt-subplots-b122bb7783ca

'''

#ax.plot(input_values, squares, linewidth = 3)
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.Reds, s=2)

#Set axis' ranges
ax.axis([1,1100,1,1100000])

#Set chart title and name axis
ax.set_title("Squared Numbers", fontsize = 24)
ax.set_xlabel("Input Values", fontsize = 14)
ax.set_ylabel("Square of values", fontsize = 14)

#Set size of tick-labels
ax.tick_params(axis = "both", labelsize = 14)

plt.show()