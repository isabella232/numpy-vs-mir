import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter, LinearLocator

from ..GaussSeidel.GaussSeidel import gauss_seidel
from ..GaussSeidel.GaussSeidel_RB import GS_RB
from ..multigrid import poisson_multigrid, general_multigrid
from .operators import poisson_operator_2D


def initMap_2D(dimension):
    U = np.random.uniform(0, 1, (dimension, dimension))
    U[:, -1] = 0
    U[-1, :] = 0
    U[:, 0] = 1
    U[0, :] = 1
    return U


def initMap_3D(dimension):
    U = np.random.uniform(0, 1, (dimension, dimension, dimension))
    U[:, -1, :] = 0
    U[-1, :, :] = 0
    U[:, :, -1] = 0
    U[:, 0, :] = 1
    U[0, :, :] = 1
    U[:, :, 0] = 1
    return U


def heat_sources_2D(dimension):
    F = np.zeros((dimension, dimension))
    F[:, -1] = 0
    F[-1, :] = 0
    F[:, 0] = 1
    F[0, :] = 1
    F[dimension // 2, dimension // 2] = 1
    return F


def draw2D(map):
    plt.imshow(map, cmap='RdBu_r', interpolation='nearest')
    plt.show()


def draw3D(map):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the surface.
    for index, x in np.ndenumerate(map):
        if x > 0.5:
            ax.scatter(*index, c='black', alpha=max(x - 0.5, 0))

    fig.show()
