import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm


class Visualizer:

    @staticmethod
    def x_t_diagram(diff_eq):
        solution = diff_eq.get_solution()
        ls = sum(solution.get_u(), [])
        grid = solution.get_grid()
        extent = [*grid.get_x_lim(), *grid.get_t_lim()]
        fig, ax = plt.subplots()
        image = ax.imshow(solution.get_u(), cmap=cm.coolwarm, origin='lower', extent=extent, vmin=min(ls), vmax=max(ls),
                          aspect="auto")
        cbar = fig.colorbar(image, ax=ax, fraction=.1)
        cbar.set_label(r'$U$, значение функции')

        ax.set_xlabel(r'$x$, координата')
        ax.set_ylabel(r'$t$, время')

        plt.title(Visualizer.get_ps_test(diff_eq))

        plt.show()

    @staticmethod
    def get_ps_test(diff_eq):

        ps_text = ''
        if diff_eq.get_border_conditions().get_type_of_boundary_condition() == 'periodic':
            ps_text = 'c периодическими граничными условиями'
        elif diff_eq.get_border_conditions().get_type_of_boundary_condition() == 'outflow':
            ps_text = 'c граничными условиями типа выток'
        return f"Решение {ps_text}"

    @staticmethod
    def plot_solution(diff_eq, temporary_layers=None, num_plot=3):

        solution = diff_eq.get_solution()

        if type(temporary_layers) is int:
            temporary_layers = [temporary_layers]

        if temporary_layers is None:
            num_step_t = diff_eq.get_solution().get_grid().get_num_step_t()
            temporary_layers = range(0, num_step_t, int(num_step_t / num_plot))

        fig, ax = plt.subplots()
        for t in temporary_layers:
            result = solution[t]
            u = result[1:]
            ax.plot(*u, label=rf'$t = {result[0]:.2f}$')

        ax.legend(loc=2)
        ax.set_xlabel(r'$x$, координата')
        ax.set_ylabel(r'$U$, значение функции')
        plt.title(Visualizer.get_ps_test(diff_eq))
        plt.show()

    @staticmethod
    def plot_solution_surface(diff_eq):

        solution = diff_eq.get_solution()
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

        plt.title(Visualizer.get_ps_test(diff_eq))

        plt.show()
