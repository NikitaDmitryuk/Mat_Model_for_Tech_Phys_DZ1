from solution import Solution


class BorderConditions:

    """
    periodic - периодичные граничные условия
    outflow - выток
    """

    def __init__(self, left_bc=lambda t: 0, right_bc=lambda t: 0, type_of_boundary_condition=None):
        self.left_bc_ = left_bc
        self.right_bc_ = right_bc
        self.type_of_boundary_condition_ = type_of_boundary_condition

    def set_left_bc(self, left_bc):
        self.left_bc_ = left_bc

    def set_right_bc(self, right_bc):
        self.right_bc_ = right_bc

    def get_left_bc(self, t):
        return self.left_bc_(t)

    def get_right_bc(self, t):
        return self.right_bc_(t)

    def boundary_condition_handler(self, solution: Solution):
        solution.get_u_n(-1).insert(0, self.left_bc_(solution.get_last_time()))
        solution.get_u_n(-1).append(self.right_bc_(solution.get_last_time()))

    def get_type_of_boundary_condition(self):
        return self.type_of_boundary_condition_
