#!/usr/bin/env python
from differential_equation import DifferentialEquation
from border_conditions import BorderConditions
from scheme_dz1 import SchemeDZ1
from grid import Grid
from visualizer import Visualizer

scheme = SchemeDZ1()
Visualizer.scheme_analysis(scheme, 'SchemeDZ1', c_range=(0, 1.4), k_dx_range=(-2, 2))


def initial_conditions_1(x):
    """
    U = exp(- x^2 / 2) + 2 * exp(- (x - 1) ^ 2 / 2)
    """
    from math import exp
    u1 = 1
    u2 = 2
    return u1 * exp(- x ** 2 / 2) + u2 * exp(- (x - 1) ** 2 / 2)


def initial_conditions_2(x):
    """
    u1 , 1 <= x <= 2
    """
    u1 = 1
    return u1 if 1 <= x <= 2 else 0


##############

step = 0.05
c = 0.5  # константа С в условии задачи
x0 = -4
xn = 5
t0 = 0
tn = 15

###############

scheme = SchemeDZ1(c)
border_conditions_periodic = BorderConditions(type_of_boundary_condition='periodic')  # periodic, outflow

grid1 = Grid(x0=x0, xn=xn, t0=t0, tn=tn, step_x=step, step_t=step)

diff_eq = DifferentialEquation(scheme=scheme,
                               initial_conditions=initial_conditions_1,
                               border_conditions=border_conditions_periodic,
                               grid=grid1)

diff_eq.solve_eq()

Visualizer.plot_solution(diff_eq, 1)  # temporary_layers=[0, 10, 70, 80, 90, 99], num_plot=3
Visualizer.plot_solution_surface(diff_eq, 1)
Visualizer.x_t_diagram(diff_eq, 1)

border_conditions_outflow = BorderConditions(type_of_boundary_condition='outflow')  # periodic, outflow
diff_eq.set_border_conditions(border_conditions_outflow)
diff_eq.solve_eq()

Visualizer.plot_solution(diff_eq, 2)  # temporary_layers=[0, 10, 70, 80, 90, 99], num_plot=3
Visualizer.plot_solution_surface(diff_eq, 2)
Visualizer.x_t_diagram(diff_eq, 2)

grid2 = Grid(x0=x0, xn=xn, t0=t0, tn=tn, step_x=step / 2, step_t=step / 2)
diff_eq.set_initial_conditions(initial_conditions_2)
diff_eq.set_grid(grid2)
diff_eq.set_border_conditions(border_conditions_periodic)

diff_eq.solve_eq()

Visualizer.plot_solution(diff_eq, 3)  # temporary_layers=[0, 10, 70, 80, 90, 99], num_plot=3
Visualizer.plot_solution_surface(diff_eq, 3)
Visualizer.x_t_diagram(diff_eq, 3)

diff_eq.set_border_conditions(border_conditions_outflow)
diff_eq.solve_eq()

Visualizer.plot_solution(diff_eq, 4)  # temporary_layers=[0, 10, 70, 80, 90, 99], num_plot=3
Visualizer.plot_solution_surface(diff_eq, 4)
Visualizer.x_t_diagram(diff_eq, 4)
