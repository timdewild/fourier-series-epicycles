import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# to be able to find matnimation directory
sys.path.append(os.path.abspath(''))

from core.curve_from_svg import SVGToCurve
from core.fourier_coefficients_integrator import NumericalFourierCoeffients

PI = SVGToCurve('fourier_drawings/pi_symbol/pi.svg')

xdata, ydata = PI.get_xydata()

trace_function = PI.get_trace_function()

t = np.linspace(0,1,1000)

order = 60

numerical_fourier_coeff = NumericalFourierCoeffients(
    func = trace_function,
    order = order
)

coeff_list = numerical_fourier_coeff.compute_coefficients()
np.save(f'fourier_drawings/pi_symbol/pi_symbol_coefficients_{order}', coeff_list)
trace_partial = numerical_fourier_coeff.partial_fourier_series(time_array = t)

plt.plot(xdata, ydata)
plt.plot(trace_partial.real, trace_partial.imag)
plt.gca().set_aspect('equal')
plt.savefig('fourier_drawings/pi_symbol/pi.jpg')