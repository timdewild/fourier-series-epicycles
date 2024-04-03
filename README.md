# Fourier Epicycles Animation
In these animations (made using [matnimation](https://github.com/timdewild/matnimation/tree/0e42db803f603951173fe5f804372a60ae76513c)), we give a different interpretation to (complex) Fourier series in terms of rotating vectors in the complex plane, based on the wonderful [video](https://www.youtube.com/watch?v=r6sGWTCMz2k) by 3Blue1Brown. This gives a completely new way of looking at Fourier series. We will also show how we can make 2D 'Fourier drawings' using this interpretation. An example of this 'Fourier drawing' is given by the Github cat below:

https://github.com/timdewild/fourier-series-epicycles/assets/93600756/e4a1b983-89bc-48ed-82c2-dce654978201

## The Complex Fourier Series
For a (possibly complex) function $f(t)$ with period $P$, i.e. $f(t) = f(t+P)$, the complex Fourier series is given by:
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

In general, we can associate a vector rotating in the complex plane with each term in the series. The initial orientation and length of the vector is dictated by the coefficient $c_n$. The rotation speed and direction are set by the complex phase $e^{i2\pi n t/P}$. Now, the Fourier series is a sum of the terms, which, in the language of vectors, amounts to adding the vectors tip to tail. In connecting the vectors in this way, each tip traces out an epicycle: a circle whose origin is itself moving along the perimeter of another circle. The position of the tip of the last vector in the complex plane represents the value of the series (at any given $t$). For the sine example above, note that the final tip moves only along the real axis, ranging from -1 to 1. This is to be expected, the sine function is a real function with range $[-1,1]$. This is animated in the animation below as well, the red dot indicates the tip of the final vector. 

https://github.com/timdewild/fourier-series-epicycles/assets/93600756/5ad55a88-4528-4fd7-99b6-9eefabb52b62

Note that in the sine example, $f(t)$ gives real output for every value of $t$. To show how the sine function is generated from the rotating vectors, we rotate the complex plane by 90 degrees in counter-clockwise direction (right panel). For each value of $t$, we plot the output of the series (the real value corresponding to the red dot in the right panel) in the left panel. 

https://github.com/timdewild/fourier-series-epicycles/assets/93600756/bd684643-61c1-479e-aba7-8d063129c60d

# Fourier Series for Analytic Functions
The sine example above is easy, in the sense that we only needed two non-zero terms to represent the entire series. In most cases, we can approximate the analytic function by taking the partial fourier sum:
```math
f_N(t) = \sum _{n=-N}^N c_n\; e^{i2\pi n t/P}.
```
Typically, the magnitude of the coefficients decreases with $|n|$. Therefore, we expect the partial series to better represent the actual function as we increase $N$. Below, we show how partial Fourier series for the step function and quadratic function are generated using rotating vectors. 

https://github.com/timdewild/fourier-series-epicycles/assets/93600756/7772e1d6-e628-4856-b597-6993d4f42018

https://github.com/timdewild/fourier-series-epicycles/assets/93600756/da7186fd-3818-4b87-8328-bc46a8e2d635

# Fourier Drawings
Note that the complex plane has essentially two degrees of freedom: the real axis and the complex axis. In the examples above, we only used the real degree of freedom, since we were concerned with the Fourier series for real functions. How can we use this second degree of freedom? It turns out that you can draw arbitrarely complex 2D shapes, as long as they are described by a single closed parametric curve. The curve should be closed because Fourier series only work for periodic functions: going along the closed curve once corresponds to one period. More specifically, suppose the closed parameteric curve is described by $(x(t), y(t))$, where $t$ is called the parameter. Periodicity implies that:
```math
\begin{align}
    x(t) &= x(t+P)\nonumber\\
    y(t) &= y(t+P)
\end{align}
```
We will assume that the period is $P=1$, so that the parameter ranges over $t\in [0,1]$. In the complex plane, the parametric curve can be represented by:
```math
\begin{equation*}
    f(t) = x(t) + iy(t),\quad\quad \mathrm{Re}\; f(t) = x(t),\quad\quad \mathrm{Im}\; f(t) = y(t). 
\end{equation*}
```
Now that we have $f(t)$, it is game on: we plug it into the equation for $c_n$ and we can construct the complex Fourier series. The same interpretation in terms of rotating vectors in the complex plane still applies. The difference is that now the tip of the final vector will trace out some shape in the complex plane as $t$ evolves forward, instead of staying on the real axis. This should not come as a surprise: after all in this case the function $f(t)$ is complex. In the example below, we draw a Fourier series approximations to the symbol $\pi$. Note that increasing $N$ indeed results in more accurately drawing $\pi$. 

### Drawing $\pi$ with $N = 20$
https://github.com/timdewild/fourier-series-epicycles/assets/93600756/cc613b47-0b65-43bb-bf81-ef7df4838d3d

### Drawing $\pi$ with $N = 40$
https://github.com/timdewild/fourier-series-epicycles/assets/93600756/55b98674-98c4-4c6c-b39a-8fb02ceb20b0

### Drawing $\pi$ with $N = 60$
https://github.com/timdewild/fourier-series-epicycles/assets/93600756/8d8b37a4-b17f-4bb6-b96a-92db9339427a

## A Recipe for Finding Parametric Curves of Shapes
Careful readers might have noticed that there is one, more practical, missing piece to this puzzel. For the symbol or 'shape' $\pi$, how do we find the parametric equations $x(t)$ and $y(t)$? We take an image of the symbol $\pi$ in Scalable Vector Graphics format `*.svg`. The advantage of this image format is that the shape it describes can be easily converted into a closed parametric curve, as done by the `SVGToCurve` class. This class represents $f(t)$ by an interpolation function. That is, the analytic form is not known and hence the coefficients $c_n$ can only be computed numerically, which is done using the `NumericalFourierCoeffients` class. Given $c_n$ the evolution of all the vectors is calculated in the class `FourierVectorsEvolution`. 
