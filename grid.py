
import numpy as np


class Grid:

    def __init__(self, x0=0, xn=1, t0=0, tn=1, step_x=0.01, step_t=0.01):
        self.x0_ = x0
        self.xn_ = xn
        self.t0_ = t0
        self.tn_ = tn
        self.step_x_ = step_x
        self.step_t_ = step_t
        self.num_step_x_ = round((self.xn_ - self.x0_) / self.step_x_)
        self.num_step_t_ = round((self.tn_ - self.t0_) / self.step_t_)
        self.x_list_ = []
        self.t_list_ = []
        self.generate_mesh()

    def generate_mesh(self):
        self.x_list_ = np.linspace(self.x0_, self.xn_, self.num_step_x_)
        self.t_list_ = np.linspace(self.t0_, self.tn_, self.num_step_t_)

    def get_x_list(self):
        return self.x_list_

    def get_t_list(self):
        return self.t_list_

    def get_num_step_x(self):
        return self.num_step_x_

    def get_num_step_t(self):
        return self.num_step_t_

    def get_t_index(self, index):
        return self.t_list_[index]

    def get_x_index(self, index):
        return self.x_list_[index]

    def get_step_t(self):
        return self.step_t_

    def get_step_x(self):
        return self.step_x_
