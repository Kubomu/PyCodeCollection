# Importing the pyplot module from matplotlib for creating plots
import matplotlib.pyplot as pyplot

# Define the labels for the pie chart segments
labels = ('Python', 'Java', 'Scala', 'C#')

# Define the sizes for each segment, representing their proportions
sizes = [45, 20, 15, 20]

# Create a pie chart
pyplot.pie(
    sizes,                # The data values for the pie chart
    labels=labels,        # The labels corresponding to each segment
    autopct='%1.1f%%',    # Format for displaying percentages on the chart
    counterclock=False,   # Draw the segments in a clockwise direction
    startangle=105        # Starting angle for the first segment
)

# Display the pie chart
pyplot.show()
