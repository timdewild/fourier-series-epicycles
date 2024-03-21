import numpy as np
import matplotlib.pyplot as plt


class FourierVectorsEvolution:

    def __init__(self, fourier_coefficients: np.ndarray, time_array: np.ndarray):
        self.fourier_coefficients = fourier_coefficients #format [..., c_-2, c_-1, c_0, c_1, c_2, ...], must contain odd number of elements 
        self.time_array = time_array

        self.number_of_coefficients = len(self.fourier_coefficients)
        self.number_of_timesteps = len(self.time_array)

        if (self.number_of_coefficients % 2) == 0:
            raise ValueError("The array passed to 'fourier_coefficients' contains an even number of elements, should be odd!")

        self.order = (self.number_of_coefficients - 1) // 2 

        self.array_n = np.linspace(-self.order, self.order, self.number_of_coefficients, dtype = int)

        self.evolution_matrix = None

    def order_coefficients(self, array: np.ndarray):
        ordered_array = np.zeros_like(array)

        coefficient_0 = array[self.order]                                           # this is c0
        positive_coefficients = array[self.order + 1:]                              # these are [c1, c2, ..., cn]
        negative_ceofficients = np.flipud(array[:self.order])                       # these are [c-1, c-2, ..., c-n]

        ordered_array[0] = coefficient_0
        ordered_array[1::2] = negative_ceofficients
        ordered_array[2::2] = positive_coefficients

        return ordered_array

    def fourier_terms_evolution(self):
        self.evolution_matrix = np.zeros((self.number_of_coefficients, self.number_of_timesteps))

        ordered_fourier_coefficients = self.order_coefficients(self.fourier_coefficients)
        ordered_array_n = self.order_coefficients(self.array_n)
        
        product_nt = ordered_array_n[:, np.newaxis] * self.time_array[np.newaxis, :]

        # first compute the evolution matrix with basis functions exp(2pi * i * nt) only
        # rows: n-values cols: t-values
        self.evolution_matrix = np.exp(1j * 2 * np.pi * product_nt)

        # then multiply by the respective each row by the corresponding coefficient cn 
        self.evolution_matrix = ordered_fourier_coefficients[:, np.newaxis] * self.evolution_matrix

        # then take the cumulative sum along each column to find the coordinates of the tips of the vector in the chain at all timesteps
        self.evolution_matrix = np.cumsum(self.evolution_matrix, axis = 0)

        return self.evolution_matrix
    
def complex_coefficients_square_wave(n: int):
    if n == 0:
        cn = 0

    else:
        cn = 1j / (np.pi * n) * ( (-1) ** n - 1 )

    return cn 

order = 13
coefficients = [complex_coefficients_square_wave(k) for k in np.linspace(-order, order, 2 * order + 1)]
coefficients = np.asarray(coefficients)

time = np.linspace(0,1,100)

test = FourierVectorsEvolution(
    fourier_coefficients = coefficients, 
    time_array = time
    )

evolution = test.fourier_terms_evolution()

#print(evolution)
print(evolution[:,0])
print(evolution[:,10])

tindex = 8
x, y = evolution[:,tindex].real, evolution[:,tindex].imag

plt.plot(x, y)
plt.xlim(0,1.5)
plt.ylim(-0.5,0.5)
plt.gca().set_aspect('equal')
plt.show()






# a = np.array([1,2,3,4])
# b = np.array([1,2,3])

# print(a[:, np.newaxis] * b[np.newaxis, :])


# flist = np.array(['c-2','c-1','c0','c1','c2'])

# test = FourierVectorsEvolution(
#     fourier_coefficients = np.array([1,1,1,1,1]), 
#     time_array = np.array([0, 0.25, 0.5, 0.75, 1])
#     )

# test.fourier_terms_evolution()


# test_matrix = np.array([[1,1,1], [1,1,1], [1,1,1]])
# print(np.cumsum(test_matrix, axis = 0))
# test_vec = np.array([1,2,3])
# print(test_matrix)
# print(test_vec[:, np.newaxis])
# print(test_vec[:, np.newaxis] * test_matrix)
        
# test = np.ones((4,3))
# print(np.array([1,2,3,4])[:, np.newaxis] * test)

        

