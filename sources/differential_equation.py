
from visualizer import Visualizer
from solution import Solution


class DifferentialEquation:

    def __init__(self, scheme, initial_conditions, border_conditions, grid):
        self.scheme_ = scheme
        self.initial_conditions_ = initial_conditions
        self.border_conditions_ = border_conditions
        self.grid_ = grid
        self.solution_ = Solution(initial_conditions, grid)

    def set_grid(self, grid):
        self.grid_ = grid

    def solve_eq(self):
        if self.grid_ is not None:
            self.solution_ = self.scheme_.solve(self.grid_, self.initial_conditions_, self.border_conditions_)
        else:
            print("Не задана область расчета")

    def diff_eq_visualization(self, temporary_layers=0, surface=False):
        Visualizer.plot_solution(self.solution_, temporary_layers, surface)
