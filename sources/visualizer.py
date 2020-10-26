
import matplotlib.pyplot as plt
from solution import Solution
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm


class Visualizer:

    @staticmethod
    def plot_solution(solution: Solution, temporary_layers, surface):
        if surface:
            Visualizer.plot_solution_surface(solution)
            return

        if type(temporary_layers) is int:
            temporary_layers = [temporary_layers]

        fig, ax = plt.subplots()
        for t in temporary_layers:
            u = solution[t][1:]
            ax.plot(*u)

        plt.show()

    @staticmethod
    def plot_solution_surface(solution: Solution):

        ls = sum(solution.get_u(), [])

        z = np.asarray(ls)
        x_surf, t_surf = np.meshgrid(solution.get_grid().get_x_list(), solution.get_grid().get_t_list())
        z_surf = z.reshape(x_surf.shape)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x_surf, t_surf, z_surf, cmap=cm.coolwarm)
        ax.set_xlabel(r'$x$, координата')
        ax.set_ylabel(r'$t$, время')
        ax.set_zlabel(r'$U$, значение функции')
        plt.show()
