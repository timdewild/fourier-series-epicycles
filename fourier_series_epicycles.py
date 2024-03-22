import numpy as np

import sys
import os

abs_path = 'matnimation'
sys.path.append(os.path.abspath(abs_path)) 

from matnimation.src.matnimation.animation.animation import Animation
from matnimation.src.matnimation.canvas.single_canvas import SingleCanvas
from matnimation.src.matnimation.artist.animated.animated_line import AnimatedLine
from matnimation.src.matnimation.artist.static.static_line import StaticLine
from matnimation.src.matnimation.artist.animated.animated_circle import AnimatedCircle

from fourier_vectors_evolution import FourierVectorsEvolution

def complex_coefficients_square_wave(n: int):
    if n == 0:
        cn = 0

    else:
        cn = 1j / (np.pi * n) * ( (-1) ** n - 1 )

    return cn 

order = 20
coefficients = [complex_coefficients_square_wave(k) for k in np.linspace(-order, order, 2 * order + 1)]
coefficients = np.asarray(coefficients)

time = np.linspace(0,1,1000)

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
canvas = SingleCanvas(
    figsize = (4,4),
    dpi = 400,
    time_array = time,
    axis_limits = [-2,2,-2,2],
    axis_labels = ['$x$','$y$']
)

canvas.save_canvas('testcanvas.jpg')

vectors = AnimatedLine(
    name = 'vectors',
    x_data = ydata,
    y_data = xdata
)

vectors.set_styling_properties(linewidth = 0.5)

canvas.add_artist(vectors)

for i in range(1,2 * order + 1):
    x_center = ydata[i - 1, :]
    y_center = xdata[i - 1, :]
    cycle_radius = cycles_radii[i]

    cycle = AnimatedCircle(
        name = f"cycle-{i}",
        radius = cycle_radius,
        x_data = x_center,
        y_data = y_center
    )

    canvas.add_artist(cycle)

    cycle.set_styling_properties(linewidth = 0.2, edgecolor = 'k', facecolor = 'None', alpha = 0.5)

x_dot = ydata[-1, :]
y_dot = xdata[-1, :]

tracing_dot = AnimatedCircle(
    name = 'Tracing Dot',
    radius = 0.015,
    x_data = x_dot,
    y_data = y_dot
)

canvas.add_artist(tracing_dot)

tracing_dot.set_styling_properties(edgecolor = 'tab:red', facecolor = 'tab:red')




animation = Animation(canvas, interval = 10)

animation.render('animation.mp4')

