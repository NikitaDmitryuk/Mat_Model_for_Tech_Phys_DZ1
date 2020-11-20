
class Solution:

    def __init__(self, initial_conditions, grid):
        self.grid_ = grid
        self.solution_ = [list(map(initial_conditions, grid.get_x_list()))]

    def add_new_temporary_layer(self, new_temporary_layer):
        self.solution_.append(list(new_temporary_layer))

    def __getitem__(self, item):
        return list([self.grid_.get_t_index(item), self.grid_.get_x_list(), self.solution_[item]])

    def get_u_ni(self, n, i):
        return self.solution_[n][i]

    def get_u_n(self, n):
        return self.solution_[n]

    def get_last_time(self):
        return self.grid_.get_t_index(len(self.solution_) - 1)

    def get_u(self):
        return self.solution_

    def get_grid(self):
        return self.grid_
