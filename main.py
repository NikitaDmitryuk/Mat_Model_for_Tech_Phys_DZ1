
from differential_equation import DifferentialEquation
from border_conditions import BorderConditions
from scheme_dz1 import SchemeDZ1
from grid import Grid
from math import exp
from visualizer import Visualizer


def initial_conditions(x):
    """
    U = exp(- x^2 / 2) + 2 * exp(- (x - 1) ^ 2 / 2)
    """
    u1 = 1
    u2 = 2
    return u1 * exp(- x ** 2 / 2) + u2 * exp(- (x - 1) ** 2 / 2)


##############

step = 0.05
c = 0.5  # константа С в условии задачи
x0 = -4
xn = 5
t0 = 0
tn = 15

###############

scheme = SchemeDZ1(c)
border_conditions = BorderConditions(type_of_boundary_condition='periodic')  # periodic, outflow

grid = Grid(x0=x0, xn=xn, t0=t0, tn=tn, step_x=step, step_t=step)

diff_eq = DifferentialEquation(scheme=scheme,
                               initial_conditions=initial_conditions,
                               border_conditions=border_conditions,
                               grid=grid)

diff_eq.solve_eq()

Visualizer.plot_solution_surface(diff_eq)
Visualizer.plot_solution(diff_eq)  # temporary_layers=[0, 10, 70, 80, 90, 99], num_plot=3
