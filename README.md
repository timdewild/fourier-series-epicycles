# Fourier Epicycles Animation
In these animations, we give a different interpretation to (complex) Fourier series in terms of rotating vectors in the complex plane. This gives a completely new way of looking at Fourier series. We will also show how we can make 2D 'Fourier drawings' using this interpretation. 

## The Complex Fourier Series
For a function $f(t)$ with period $P$, i.e. $f(t) = f(t+P)$, the complex Fourier series is given by:
```math
\begin{equation*}
    f(t) = \sum_{n=-\infty}^{+\infty} c_n\; e^{i2\pi n t/P}.
\end{equation*}
```
In practice, finding the series amounts to computing the (complex) Fourier coefficients $c_n$, which are defined via:
```math
\begin{equation*}
    c_n = \frac{1}{P} \int_0^P  dt\; f(t)\; e^{-i2\pi n t/P}.
\end{equation*}
```

As an example, we will compute the complex Fourier series for the function $f(t)=\sin(2\pi t)$. The period of this function is $P=1$. The next step would be to insert $f(t)$ into $c_n$ and calculate away. However, in our case, we can be smarter. By Euler's identity we have:
```math
\sin(x) = \frac{e^{ix}-e^{-ix}}{2i},
```
and hence we find:
```math
f(t) = \frac{1}{2i} e^{i2\pi t} - \frac{1}{2i} e^{-i2\pi t} = -\frac{i}{2} e^{i2\pi t} + \frac{i}{2} e^{-i2\pi t}.
```
From the final form, we infer that $c_{\pm 1} = \mp i/2$ and $c_{n\neq \pm 1} = 0$. 

## Rotating-Vectors Interpretation
We can also interpret complex Fourier series as a collection of vectors rotating in the complex plane. Take for example the $n=1$ term from the example above. At $t=0$, it can be represented as a vector pointing from the origin to $-i/2$. As $t$ evolves from 0 to 1, the vector rotates in the counter-clockwise direction in the complex plane. The same applies to the $n=-1$ term, but now we rotate in clockwise direction and the vector-tip starts at $+i/2$. 

In general, we can associate a vector rotating in the complex plane with each term in the series. The initial orientation and length of the vector is dictated by the coefficient $c_n$. The rotation speed and direction are set by the complex phase $e^{i2\pi n t/P}$. Now, the Fourier series is a sum of the terms, which, in the language of vectors, amounts to adding the vectors tip to tail. In connecting the vectors in this way, each tip traces out an epicycle: a circle whose origin is itself moving along the perimeter of another circle. The position of the tip of the last vector in the complex plane represents the value of the series (at any given $t$). For the sine example above, note that the final tip moves only along the real axis, ranging from -1 to 1. This is to be expected, the sine function is a real function with range $[-1,1]$.  