import math
import pygal
import random

line_chart = pygal.Line()
line_chart.title = 'lines'
days = 7
line_chart.x_labels = map(str, range(0, 360*days))
y_vals = []
y_range = 100
thing = 360
for nmb in range(days):
    start = nmb*thing
    end = nmb*thing + thing
    start_rand = random.randint(2,5)
    end_rand = random.randint(2,5)
    up_slope = random.randint(1,20)
    dn_slope = random.randint(1,20)
    for x in range(start, end):
        half = (end + start) // 2
        fact = 1
        if x < half:
            fact = random.random() * 3
        else:
            fact = random.random() * 3
        y = math.sin(math.radians(x)) * fact
        if nmb == 3 or nmb == 4:
            y = y / 2
        else:
            y = y * 2
        if y < 0:
            y = y / 2
        # randoms
        y = (y + 10) * 100
        # change slope
        y_vals.append(y)
line_chart.add('line', y_vals)
line_chart.render_to_png('snoos.png')
