
from collections.abc import Callable
import numpy as np

class Term:
    def __init__(self, value, name='', children=(), op: Callable =lambda k: k):
        self.value = value
        self.name = name
        self.children = children
        self.op = op

    def __str__(self):
        if isinstance(self.value, float) or isinstance(self.value, int):
            if self.name:
                return f'{self.name}: {self.value:.3f}'
            return f'({self.value:.3f})'
        return str(self.value)

    def __add__(self, other):
        return Term(self.value + other.value, children=(self, other), op=self.__add__)

    def __sub__(self, other):
        return Term(self.value - other.value, children=(self, other), op=self.__sub__)

    def __mul__(self, other):
        return Term(self.value * other.value, children=(self, other), op=self.__mul__)

    def __truediv__(self, other):
        return Term(self.value / other.value, children=(self, other), op=self.__truediv__)

    def cos(self):
        return Term(np.cos(self.value), children=(self,), op=self.cos)

    def sin(self):
        return Term(np.sin(self.value), children=(self,), op=self.sin)

    def refresh(self):
        if len(self.children) == 1:
            self.children[0].refresh()
            self.value = self.op().value
        if len(self.children) == 2:
            self.children[0].refresh()
            self.children[1].refresh()
            self.value = self.op(self.children[1]).value
        return 