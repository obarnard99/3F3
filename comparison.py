import numpy as np
import matplotlib.pyplot as plt
from pdfs import n_pdf, u_pdf
from smoothing import ksdensity
import math


dist = 'n'
smoothed = True
width = 0.1
img_name = 'smoothed_normal01.png'


def uniform_plot(a, b):
    p = u_pdf(a, b)
    range = b - a
    plt.plot([a, b], [p, p], color='darkorange', ls='--', label='Exact Uniform Dist.')
    plt.plot([a - range / 4, a], [0, 0], color='darkorange', ls='--')
    plt.plot([b, b + range / 4], [0, 0], color='darkorange', ls='--')
    plt.plot([a, a], [0, p], color='darkorange', ls='--')
    plt.plot([b, b], [0, p], color='darkorange', ls='--')


if dist == 'n':
    # Plot normal distribution
    J = 30
    x_range = 10
    N = 1000
    x_rand = np.random.randn(N)
    x_lin = np.linspace(-(x_range / 2), x_range / 2, N)
    if smoothed:
        ks_density = ksdensity(x_rand, width=width)
        plt.plot(x_lin, ks_density(x_lin), color='cornflowerblue', label='Smoothed Approximation')
    else:
        plt.hist(x_rand, bins=J, color='cornflowerblue', density=True, label='Histogram Approximation')
    plt.plot(x_lin, n_pdf(x_lin), color='darkorange', ls='--', label='Exact Normal Dist.') # normal plot
    plt.legend()

elif dist == 'u':
    # Plot uniform distribution
    a = 0
    b = 1
    p = u_pdf(a, b)
    J = 20
    N = 1000
    x_rand = np.random.rand(N)
    x_lin = np.linspace(-0.5, 1.5, N)
    if smoothed:
        ks_density = ksdensity(x_rand, width=width)
        plt.plot(x_lin, ks_density(x_lin), color='cornflowerblue', label='Smoothed Approximation')
    else:
        plt.hist(x_rand, bins=J, color='cornflowerblue', density=True, label='Histogram Approximation')
    uniform_plot(a, b)
    #plt.plot(x_lin, n_pdf(x_lin), color='red', ls='--') # normal plot
    plt.legend()

plt.xlabel('x')
plt.ylabel('Normalised Count')
plt.savefig('C:\\Users\\obarn\\Google Drive\\Cambridge\\Part IIA\\3F3\\assets\\' + img_name)
plt.show()
