
from collections.abc import Callable
import numpy as np

class Arith:
    def __init__(self, value:float, name='', children=(), op: Callable =lambda k: k):
        self.value = value
        self.name = name
        self.children = children
        self.op = op

    def __str__(self):
        return f'{self.value:.3f}'

    def __repr__(self):
        return f'{self.value:.3f}'

    def __add__(self, other):
        return Arith(self.value + other.value, children=(self, other), op=self.__add__)

    def __mul__(self, other):
        return Arith(self.value * other.value, children=(self, other), op=self.__mul__)

    def __truediv__(self, other):
        return Arith(self.value / other.value, children=(self, other), op=self.__truediv__)

    def cos(self):
        return Arith(np.cos(self.value), children=(self,), op=self.cos)

    def sin(self):
        return Arith(np.sin(self.value), children=(self,), op=self.sin)

    def refresh(self):
        if len(self.children) == 1:
            self.children[0].refresh()
            self.value = self.op().value
        if len(self.children) == 2:
            self.children[0].refresh()
            self.children[1].refresh()
            self.value = self.op(self.children[1]).value
        return 