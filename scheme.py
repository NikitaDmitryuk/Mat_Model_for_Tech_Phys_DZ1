from abc import ABC, abstractmethod


class Scheme(ABC):

    @abstractmethod
    def solve(self, grid, initial_conditions, border_conditions):
        """Решение дифференциального уравнения"""
