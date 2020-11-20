from abc import ABC, abstractmethod


class Scheme(ABC):

    @abstractmethod
    def solve(self, grid, initial_conditions, border_conditions):
        """Решение дифференциального уравнения"""

    @abstractmethod
    def get_abs_q(self):
        """Модуль характерестического уравнения"""

    @abstractmethod
    def get_abs_gamma(self):
        """Модуль фазовой скорости"""
