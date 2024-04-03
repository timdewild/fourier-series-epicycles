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

order = 60

coeff_list = np.load(f'fourier_drawings/pi_symbol/pi_symbol_coefficients_{order}.npy')
time_array = np.linspace(0,1,1000)

fourier_vectors_evolution = FourierVectorsEvolution(
    fourier_coefficients = coeff_list,
    time_array = time_array
)

evolution = fourier_vectors_evolution.fourier_terms_evolution()

real_data, imag_data = evolution.real, evolution.imag
cycles_radii = fourier_vectors_evolution.get_cycles_radii()

# dot of fourier sum
x_dot = real_data[-1, :]
y_dot = imag_data[-1, :]

# trace of fourier sum
x_data_trace = real_data[-1,:]
y_data_trace = imag_data[-1,:]


#--- Canvas ---#
canvas = SingleCanvas(
    figsize = (4,4),
    dpi = 400,
    time_array = time_array,
    axis_limits = [-1.5, 1.5, -1.5, 1.5],
    axis_labels = [None, None]
)

canvas.set_axis_properties(aspect = 'equal')

#--- Rotating Vectors ---#
vector_width = 0.0001
head_scale = 1.2732 * 0.07

for i in range(1, 2 * order + 1):
    x_tail_data = real_data[i - 1, :]
    y_tail_data = imag_data[i - 1, :]

    x_tip_data = real_data[i, :]
    y_tip_data = imag_data[i, :]

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

    canvas.add_artist(vector)

    vector.set_styling_properties(linewidth = 0.4, facecolor = 'k', edgecolor = 'k')

#--- Moving Cycles ---#
    
for i in range(1, 2 * order + 1):
    x_center = real_data[i - 1, :]
    y_center = imag_data[i - 1, :]
    cycle_radius = cycles_radii[i]

    cycle = AnimatedCircle(
        name = f"cycle-{i}",
        radius = cycle_radius,
        x_data = x_center,
        y_data = y_center
    )

    canvas.add_artist(cycle)

    cycle.set_styling_properties(linewidth = 0.2, edgecolor = 'k', facecolor = 'None', alpha = 0.5)

#--- Tracing Dot ---#
tracing_dot = AnimatedCircle(
    name = 'Tracing Dot',
    radius = 0.015,
    x_data = x_dot,
    y_data = y_dot
)

canvas.add_artist(tracing_dot)

tracing_dot.set_styling_properties(edgecolor = 'tab:red', facecolor = 'tab:red')

trace = AnimatedTrace(
    name = f"$f_N(t)$ for $N={order}$",
    x_data = x_data_trace,
    y_data = y_data_trace
)

trace.set_styling_properties(linewidth = 0.4, color = 'tab:red')

canvas.add_artist(trace, in_legend = False)

#---- Animation ----#
animation = Animation(canvas, interval = 10)
animation.render(f'fourier_drawings/pi_symbol/pi_symbol_animation_{order}.mp4')