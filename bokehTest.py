import random

from bokeh.driving import count
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure

UPDATE_INTERVAL = 1000
ROLLOVER = 100 # Number of displayed data points

source = ColumnDataSource({"x": [], "y": []})

@count()
def update(x):
    y = random.random()
    source.stream({"x": [x], "y": [y]}, rollover=ROLLOVER)

p = figure()
p.line("x", "y", source=source)

doc = curdoc()
doc.add_root(p)
doc.add_periodic_callback(update, UPDATE_INTERVAL)
# bokeh serve --show plot.py
