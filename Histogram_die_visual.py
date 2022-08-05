''' LEARNINGS
-Plotly-library gives visualizations to charts. Plotly makes them interactive and device-friendly
-Bar-class is a data-set that is to be displayed in bars.
-Layout-class returns an object for the layout and configuration of the intended chart
-offline.plot()-function displays the chart and requires chart's data, layout, and the file-name
by which the chart is going to be displayed.

'''

from plotly.graph_objs import Bar, Layout
from plotly import offline

from Histogram_die import Die

'''Die for program'''
my_die = Die(6)

'''Addition of sample-rolls into a list'''
list_of_rolls = []
for roll in range(1000):
    list_of_rolls.append(my_die.roll())

'''Roll analysis - how many times each figure'''
frequencies = {}

for roll in list_of_rolls:
    if roll not in frequencies:
        frequencies[roll] = 1
    else:
        frequencies[roll] += 1

#print(frequencies)

'''Visualize results'''
x_values = list(range(1, my_die.nr_sides+1))
y_values = []
for throw in x_values:
    y_values.append(frequencies[throw])

data = [Bar(x = x_values, y = y_values)]

x_axis_config = {"title": "Results"}
y_axis_config = {"title": "Frequency"}

my_layout = Layout(title="Results of rolling 6-side die for 1000 times",
                   xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({"data":data, "layout":my_layout}, filename = "D6.html")