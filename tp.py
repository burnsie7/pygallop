import math
import pygal
import random

line_chart = pygal.Line()
line_chart.title = 'lines'
line_chart.x_labels = map(str, range(0, 1000))
y_vals = []
y_range = 100
for x in range(-180, 360):
    y = math.sin(math.radians(x)) * y_range + y_range
    rando = random.random() + 2
    y = math.floor(y*rando) // 2 + y_range + math.floor(rando*100) // 2 + y_range
    y_vals.append(y)
line_chart.add('line', y_vals)
line_chart.render_to_png('snoos.png')
