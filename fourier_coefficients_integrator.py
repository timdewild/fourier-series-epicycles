import numpy as np
from scipy import integrate


def complex_quadrature_integrator(integrand: callable, a: float, b: float, ):
    """
    complex function integration (done numerically), taken from https://stackoverflow.com/questions/5965583/use-scipy-integrate-quad-to-integrate-complex-numbers
    :param func: any complex function (in our case the f function for fourier transform)
    :param a: the lower limit for our integration
    :param b: the upper limit for our integration
    :return: the integral evaluation value
    """

    def real_integrand(x):
        """
        evaluate the real part of a complex function at x
        :param x: the input points
        :return: the real part of func(x)
        """
        return np.real([integrand(x_) for x_ in x])

    def imag_integrand(x):
        """
        evaluate the imaginary part of a complex function at x
        :param x: the input points
        :return: the imaginary part of func(x)
        """
        return np.imag([integrand(x_) for x_ in x])

    real_integral, real_absolute_error = integrate.quadrature(real_integrand, a, b, maxiter = 500) #maxiter=1500)  # integrate real
    imag_integral, imag_absolute_error = integrate.quadrature(imag_integrand, a, b, maxiter = 500) #maxiter=1500)  # integrate imaginary

    real_relative_error = real_absolute_error / real_integral
    imag_relative_error = imag_absolute_error / imag_integral

    threshold = 1e-3

    print(f"Relative error in real and imaginary parts are {real_relative_error} and {imag_relative_error}.")

    if real_relative_error > threshold:
        print("High real integration error", real_relative_error)

    if imag_relative_error > threshold:
        print("High imaginary integration error", imag_relative_error)


    return real_integral + 1j * imag_integral  # the complex output

class NumericalFourierCoeffients:

    def __init__(self, func: callable, order: int, period: float = 1):
        
        self.order = order
        self.func = func
        self.period  = period

        self.cached_coefficients = {}

    def coefficient_integrand(self, n: int):

        def integrand(t):
            return 1 / self.period * self.func(t) * np.exp(-1j * 2 * np.pi * n * t / self.period)
        
        return integrand
    
    def fourier_coefficient_cn(self, n: int):

        integrand: callable = self.coefficient_integrand(n = n)
        
        cn = complex_quadrature_integrator(
            integrand = integrand,
            a = 0,
            b = self.period
        )

        return cn
    
    def compute_coefficients(self):
        coefficients_list = []

        for k in range(-self.order, self.order + 1):
            if k in self.cached_coefficients:
                ck = self.cached_coefficients[k]

            else:
                ck = self.fourier_coefficient_cn(n = k)

            self.cached_coefficients[k] = ck
            coefficients_list.append(ck)

    


        

    


