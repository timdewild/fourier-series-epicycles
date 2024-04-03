import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# to be able to find matnimation directory
sys.path.append(os.path.abspath(''))

from core.curve_from_svg import SVGToCurve
from core.fourier_coefficients_integrator import NumericalFourierCoeffients

github_invertocat = SVGToCurve('fourier_drawings/github_cat/github_invertocat.svg')

xdata, ydata = github_invertocat.get_xydata()

trace_function = github_invertocat.get_trace_function()

t = np.linspace(0,1,1000)

order = 60

numerical_fourier_coeff = NumericalFourierCoeffients(
    func = trace_function,
    order = order
)

coeff_list = numerical_fourier_coeff.compute_coefficients()

np.save(f'fourier_drawings/github_cat/github_cat_coefficients_{order}', coeff_list)

trace_partial = numerical_fourier_coeff.partial_fourier_series(time_array = t)

plt.plot(xdata, ydata)
plt.plot(trace_partial.real, trace_partial.imag)
plt.gca().set_aspect('equal')
plt.savefig('fourier_drawings/github_cat/github_cat.jpg')