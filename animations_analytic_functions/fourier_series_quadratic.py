import numpy as np

import sys
import os

# to be able to find matnimation directory
sys.path.append(os.path.abspath(''))

# to be able to find src directory inside matnimation
sys.path.append(os.path.abspath('matnimation'))

from matnimation.src.matnimation.animation.animation import Animation
from matnimation.src.matnimation.canvas.single_canvas import SingleCanvas
from matnimation.src.matnimation.canvas.multi_canvas import MultiCanvas
from matnimation.src.matnimation.artist.animated.animated_line import AnimatedLine
from matnimation.src.matnimation.artist.animated.animated_circle import AnimatedCircle
from matnimation.src.matnimation.artist.animated.animated_arrow import AnimatedArrow
from matnimation.src.matnimation.artist.animated.animated_trace import AnimatedTrace
from matnimation.src.matnimation.artist.static.static_hlines import StaticHlines
from matnimation.src.matnimation.artist.static.static_line import StaticLine

from core.fourier_vectors_evolution import FourierVectorsEvolution

def complex_coefficients_quadratic(n: int):
    if n == 0:
        cn = 1 / 3

    else:
        cn = 1j / 2 / np.pi / n + 1 / 2 / (np.pi * n) ** 2

    return cn 

order = 3
coefficients = [complex_coefficients_quadratic(k) for k in np.linspace(-order, order, 2 * order + 1)]
coefficients = np.asarray(coefficients)

time = np.linspace(0,1,700)

fourier_vectors_evolution = FourierVectorsEvolution(
    fourier_coefficients = coefficients, 
    time_array = time
    )

evolution = fourier_vectors_evolution.fourier_terms_evolution()

real_data, imag_data = evolution.real, evolution.imag
cycles_radii = fourier_vectors_evolution.get_cycles_radii()

# square signal 
x_signal = time
y_signal = x_signal ** 2

# dot of fourier sum
x_dot = imag_data[-1, :]
y_dot = real_data[-1, :]

# trace of fourier sum
x_data_trace = time
y_data_trace = real_data[-1,:]

# leverer 1 data
x_data_leveler_1 = np.vstack((time, np.ones_like(time)))
y_data_leveler_1 = np.vstack((y_dot, y_dot))

# leverer 2 data
x_data_leveler_2 = np.vstack((1.5 * np.ones_like(time), 0 * np.ones_like(time)))
y_data_leveler_2 = np.vstack((y_dot, y_dot))








#---- ANIMATION ---#

canvas = MultiCanvas(
    figsize = (8,4),
    dpi = 400,
    time_array = time,
    nrows = 1,
    ncols = 2,
    axes_limits = [ [0, 1, -0.2, +1.2], [0.5, -0.5, -0.2, 1.2] ],
    axes_labels = [['$t$', '$f(t)$'], ['Im $z$', 'Re $z$']]
)

canvas.set_axis_properties(row = 0, col = 0, xticks = [0, 0.25, 0.5, 0.75, 1], xticklabels = ['$0$', '', '$0.5$', '', '$1$'], yticks = [0, 0.5, 1.], yticklabels = ['$0$', '', '1'])
canvas.set_axis_properties(row = 0, col = 1, yticks = [0, 0.5, 1.], yticklabels = ['$0$', '', '1'], aspect = 'equal')

#---- Panel 1 ----#

#--- Step Function ---#
step_function = StaticLine(
    name = '$f(t) = t^2$',
    x_data = x_signal,
    y_data = y_signal
)

canvas.add_artist(step_function, row = 0, col = 0, in_legend = True)

step_function.set_styling_properties(linewidth = 0.4, color = 'tab:blue')

#--- Fourier Series ---#

trace = AnimatedTrace(
    name = f"$f_N(t)$ for $N={order}$",
    x_data = x_data_trace,
    y_data = y_data_trace
)

trace.set_styling_properties(linewidth = 0.4, color = 'tab:red')

canvas.add_artist(trace, row = 0, col = 0, in_legend = True)

#--- Leverer 1 ---#
leveler_1 = AnimatedLine(
    name = 'Leverer 1',
    x_data = x_data_leveler_1,
    y_data = y_data_leveler_1
)

canvas.add_artist(leveler_1, row = 0, col = 0)

#---- Panel 2 ----#

#--- Rotating Vectors ---#
vector_width = 0.0001
head_scale = 1.2732 * 0.07

for i in range(1, 2 * order + 1):
    x_tail_data = imag_data[i - 1, :]
    y_tail_data = real_data[i - 1, :]

    x_tip_data = imag_data[i, :]
    y_tip_data = real_data[i, :]

    head_width = head_scale * cycles_radii[i]

    vector = AnimatedArrow(
        name = f"vector-{i}",
        x_tail_data = x_tail_data,
        y_tail_data = y_tail_data,
        x_tip_data = x_tip_data,
        y_tip_data = y_tip_data,
        width = vector_width,
        head_width = head_width, 
        head_length = 1.5 * head_width
    )

    canvas.add_artist(vector, row = 0, col = 1)

    vector.set_styling_properties(linewidth = 0.4, facecolor = 'k', edgecolor = 'k')

#--- Moving Cycles ---#
    
for i in range(1, 2 * order + 1):
    x_center = imag_data[i - 1, :]
    y_center = real_data[i - 1, :]
    cycle_radius = cycles_radii[i]

    cycle = AnimatedCircle(
        name = f"cycle-{i}",
        radius = cycle_radius,
        x_data = x_center,
        y_data = y_center
    )

    canvas.add_artist(cycle, row = 0, col = 1)

    cycle.set_styling_properties(linewidth = 0.2, edgecolor = 'k', facecolor = 'None', alpha = 0.5)

#--- Red Tracing Dot 2 ---#

tracing_dot_2 = AnimatedCircle(
    name = 'Tracing Dot',
    radius = 0.015,
    x_data = x_dot,
    y_data = y_dot
)

canvas.add_artist(tracing_dot_2, row = 0, col = 1)

tracing_dot_2.set_styling_properties(edgecolor = 'tab:red', facecolor = 'tab:red')

#--- Leverer 2 ---#
leveler_2 = AnimatedLine(
    name = 'Leverer 2',
    x_data = x_data_leveler_2,
    y_data = y_data_leveler_2
)

canvas.add_artist(leveler_2, row = 0, col = 1)

for leverer in [leveler_1, leveler_2]:
    leverer.set_styling_properties(linewidth = 0.3, linestyle = 'dashed', color = 'tab:red')


#--- Legend ---#
canvas.construct_legend(row = 0, col = 0, fontsize = 'small', ncols = 2, loc = 'lower center')


#---- Animation ----#
animation = Animation(canvas, interval = 10)
animation.render('animations_analytic_functions/fourier_series_quadratic.mp4')

