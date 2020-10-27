
from solution import Solution


class DifferentialEquation:

    def __init__(self, scheme, initial_conditions, border_conditions, grid):
        self.scheme_ = scheme
        self.initial_conditions_ = initial_conditions
        self.border_conditions_ = border_conditions
        self.grid_ = grid
        self.solution_ = Solution(initial_conditions, grid)

    def set_border_conditions(self, border_conditions):
        self.border_conditions_ = border_conditions

    def get_grid(self):
        return self.grid_

    def get_scheme(self):
        return self.scheme_

    def get_initial_conditions(self):
        return self.initial_conditions_

    def get_border_conditions(self):
        return self.border_conditions_

    def get_solution(self):
        return self.solution_

    def set_grid(self, grid):
        self.grid_ = grid

    def solve_eq(self):
        if self.grid_ is not None:
            self.solution_ = self.scheme_.solve(self.grid_, self.initial_conditions_, self.border_conditions_)
        else:
            print("Не задана область расчета")
