import math
import pygal
import random

line_chart = pygal.Line()
line_chart.title = 'lines'
line_chart.x_labels = map(str, range(0, 400))
y_vals = []
y_range = 100
thing = 360
for x in range(0, thing):
    y = math.sin(math.radians(x)) * y_range + y_range
    if y < y_range:
        y = y // 4
    rando = random.random() + 2
    y = math.floor(y*rando) // 2 + y_range + math.floor(rando*100) // 2 + y_range
    if y < thing:
        y = y + 100
    y_vals.append(y)
line_chart.add('line', y_vals)
line_chart.render_to_png('snoos.png')
