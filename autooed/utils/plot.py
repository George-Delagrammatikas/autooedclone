import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pymoo.factory import get_performance_indicator


def plot_performance_space(Y):
    '''
    '''
    Y = np.array(Y)
    assert Y.ndim == 2, f'Invalid shape {Y.shape} of objectives to plot'

    if Y.shape[1] == 2:
        plt.scatter(*Y.T)
        plt.show()
    elif Y.shape[1] == 3:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.scatter(*Y.T)
        plt.show()
    else:
        raise Exception(f'Objectives with dimension {Y.shape[1]} is not supported')


def plot_hypervolume(Y):
    '''
    '''
    ref_point = np.max(Y, axis=0)
    indicator = get_performance_indicator('hv', ref_point=ref_point)
    hv_list = []
    for i in range(1, len(Y)):
        hv = indicator.calc(Y[:i])
        hv_list.append(hv)
    plt.plot(np.arange(1, len(Y)), hv_list)
    plt.show()