import numpy as np

import sys
import os

abs_path = 'matnimation'
sys.path.append(os.path.abspath(abs_path)) 

from matnimation.src.matnimation.canvas.single_canvas import SingleCanvas
from matnimation.src.matnimation.artist.animated.animated_line import AnimatedLine

canvas = SingleCanvas(
    figsize = (4,4),
    dpi = 400,
    time_array = None,
    axis_limits = [0,1,0,1],
    axis_labels = ['$x$', '$y$']
)

canvas.save_canvas('testcanvas.jpg')