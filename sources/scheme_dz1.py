from scheme import Scheme
from solution import Solution


class SchemeDZ1(Scheme):

    def __init__(self, const):
        self.solution_ = None
        self.const_ = const
        self.c = None
        self.grid_ = None

    def calc_first_time_layer(self, i):
        # c = self.c
        u0 = self.solution_.get_u_n(0)
        dt = self.grid_.get_step_x()
        dx = self.grid_.get_step_t()
        return u0[i] - self.const_ * dt * (u0[i + 1] - u0[i - 1]) / (2 * dx) +\
            self.const_ * dt * dt / 2 * (u0[i - 1] - 2 * u0[i] + u0[i + 1]) / (dx * dx)

    def calc_next_time_layer(self, n, i):
        c = self.c
        un = self.solution_.get_u_n(n)
        unm1 = self.solution_.get_u_n(n - 1)
        return 2 * c * c / (1 + c) * un[i - 1] + 2 * (1 - c) * un[i] - (1 - c) / (1 + c) * unm1[i]

    def solve(self, grid, initial_conditions, border_conditions):
        self.solution_ = Solution(initial_conditions, grid)
        self.grid_ = grid
        self.c = self.const_ * grid.get_step_t() / grid.get_step_x()
        print(f'c * dt / dx = {self.c}')

        if border_conditions.get_type_of_boundary_condition() == 'periodic':
            border_conditions.set_left_bc(lambda t: self.solution_.get_u_ni(0, -1))

        solution_1 = []
        for i in range(1, grid.get_num_step_x() - 1):
            solution_1.append(self.calc_first_time_layer(i))

        if border_conditions.get_type_of_boundary_condition() == 'outflow':
            border_conditions.set_right_bc(lambda t: solution_1[-1])
        elif border_conditions.get_type_of_boundary_condition() == 'periodic':
            border_conditions.set_left_bc(lambda t: solution_1[-1])
            border_conditions.set_right_bc(lambda t: solution_1[-1])

        self.solution_.add_new_temporary_layer(solution_1)
        border_conditions.boundary_condition_handler(self.solution_)

        for n in range(1, grid.get_num_step_t() - 1):

            solution_np1 = []

            for i in range(1, grid.get_num_step_x() - 1):
                solution_np1.append(self.calc_next_time_layer(n, i))

            if border_conditions.get_type_of_boundary_condition() == 'outflow':
                border_conditions.set_right_bc(lambda t: self.calc_next_time_layer(n, grid.get_num_step_x() - 1))
            elif border_conditions.get_type_of_boundary_condition() == 'periodic':
                border_conditions.set_left_bc(lambda t: self.calc_next_time_layer(n, grid.get_num_step_x() - 1))
                border_conditions.set_right_bc(lambda t: self.calc_next_time_layer(n, grid.get_num_step_x() - 1))

            self.solution_.add_new_temporary_layer(solution_np1)
            border_conditions.boundary_condition_handler(self.solution_)

        return self.solution_
