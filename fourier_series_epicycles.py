import numpy as np

import sys
import os

abs_path = 'matnimation'
sys.path.append(os.path.abspath(abs_path)) 

from matnimation.src.matnimation.animation.animation import Animation
from matnimation.src.matnimation.canvas.single_canvas import SingleCanvas
from matnimation.src.matnimation.canvas.multi_canvas import MultiCanvas
from matnimation.src.matnimation.artist.animated.animated_line import AnimatedLine
from matnimation.src.matnimation.artist.animated.animated_circle import AnimatedCircle
from matnimation.src.matnimation.artist.animated.animated_arrow import AnimatedArrow
from matnimation.src.matnimation.artist.animated.animated_trace import AnimatedTrace

from fourier_vectors_evolution import FourierVectorsEvolution

def complex_coefficients_square_wave(n: int):
    if n == 0:
        cn = 0

    else:
        cn = 1j / (np.pi * n) * ( (-1) ** n - 1 )

    return cn 

order = 10
coefficients = [complex_coefficients_square_wave(k) for k in np.linspace(-order, order, 2 * order + 1)]
coefficients = np.asarray(coefficients)

time = np.linspace(0,1,700)

test = FourierVectorsEvolution(
    fourier_coefficients = coefficients, 
    time_array = time
    )

evolution = test.fourier_terms_evolution()

tindex = 8
x, y = evolution[:,tindex].real, evolution[:,tindex].imag

xdata, ydata = evolution.real, evolution.imag
cycles_radii = test.get_cycles_radii()







#---- ANIMATION ---#

canvas = MultiCanvas(
    figsize = (8,4),
    dpi = 400,
    time_array = time,
    nrows = 1,
    ncols = 2,
    axes_limits = [ [0,1,-1.5,+1.5], [-1.5, 1.5, -1.5, 1.5] ],
    axes_labels = [[' ', ' '], [' ', ' ']]
)

canvas.set_axis_properties(row = 0, col = 0, xticks = [0, 0.25, 0.5, 0.75, 1], xticklabels = ['$0$', '', '$0.5$', '', '$1$'], yticklabels = ['', '$-1$', '' , '$0$', '', '$+1$', ''])
canvas.set_axis_properties(row = 0, col = 1, xticklabels = [], yticklabels = [])

canvas.save_canvas('canvas.jpg')

# canvas = SingleCanvas(
#     figsize = (4,4),
#     dpi = 400,
#     time_array = time,
#     axis_limits = [-1.5,1.5,-1.5,1.5],
#     axis_labels = [' ', ' ']
# )
# canvas.set_axis_properties(xticklabels = [], yticklabels = [])
# canvas.save_canvas('testcanvas.jpg')


vector_width = 0.0001
head_scale = 1.2732 * 0.07

for i in range(1, 2 * order + 1):
    x_tail_data = ydata[i - 1, :]
    y_tail_data = xdata[i - 1, :]

    x_tip_data = ydata[i, :]
    y_tip_data = xdata[i, :]

    head_width = head_scale * cycles_radii[i]

    vector = AnimatedArrow(
        name = f"vector-{i}",
        x_tail_data = x_tail_data,
        y_tail_data = y_tail_data,
        x_tip_data = x_tip_data,
        y_tip_data = y_tip_data,
        width = vector_width,
        head_width = head_width,       #3 * head_scale * vector_width,
        head_length = 1.5 * head_width      #1.5 * 3 * head_scale * vector_width
    )

    canvas.add_artist(vector, row = 0, col = 1)

    vector.set_styling_properties(linewidth = 0.4, facecolor = 'k', edgecolor = 'k')

print(cycles_radii[1])

for i in range(1, 2 * order + 1):
    x_center = ydata[i - 1, :]
    y_center = xdata[i - 1, :]
    cycle_radius = cycles_radii[i]

    cycle = AnimatedCircle(
        name = f"cycle-{i}",
        radius = cycle_radius,
        x_data = x_center,
        y_data = y_center
    )

    canvas.add_artist(cycle, row = 0, col = 1)

    cycle.set_styling_properties(linewidth = 0.2, edgecolor = 'k', facecolor = 'None', alpha = 0.5)

x_dot = ydata[-1, :]
y_dot = xdata[-1, :]

tracing_dot = AnimatedCircle(
    name = 'Tracing Dot',
    radius = 0.015,
    x_data = x_dot,
    y_data = y_dot
)

canvas.add_artist(tracing_dot, row = 0, col = 1)

tracing_dot.set_styling_properties(edgecolor = 'tab:red', facecolor = 'tab:red')

#---- Panel 1 ----#
x_data_trace = time
y_data_trace = xdata[-1,:]

trace = AnimatedTrace(
    name = 'Fourier series trace',
    x_data = x_data_trace,
    y_data = y_data_trace
)

canvas.add_artist(trace, row = 0, col = 0)

animation = Animation(canvas, interval = 10)

animation.render('animation.mp4')

