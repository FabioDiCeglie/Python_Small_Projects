#Bokeh basic example
from bokeh.plotting import figure, output_file, show

#The data to use for the plot, in the form of lists. Can also be Pandas dataframes.
#Both data sets should have the same length
x = [10, 20, 30, 40, 50, 60, 70, 90]
y = [11, 12, 14, 16, 17, 18, 19, 21]

#Generating the output HTML file
output_file("line.html")

#Creating a new plot with a title and axis labels
p = figure(title = "Basic Line Plot", x_axis_label = 'X-Axis', y_axis_label = 'Y-Axis')

#Adding a line renderer with a legend and setting the line thickness (width)
p.line(x, y, legend_label = "Price", line_width = 3)

#Displaying the final result
show(p)
