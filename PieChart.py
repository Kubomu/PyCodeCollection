import matplotlib.pyplot as pyplot

labels = ('Python', 'Java', 'Scala', 'C#')
sizes = [45, 20, 15, 20]
pyplot.pie(
    sizes, labels=labels, autopct='%1.1f%%', counterclock = False, startangle=105
    )


pyplot.show()

