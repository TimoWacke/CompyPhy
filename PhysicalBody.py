from ArithmeticFunction import Arith
from DifferentialEquation import diffEq
import numpy as np


class Body:
    def __init__(self, name, properties: list[Arith] = []):
        self.name = name
        self.props = {}
        self.differentials = [] #diffEq's
        usednames = []
        for a in properties:
            if a.name:
                assert a.name not in usednames
                usednames.append(a.name)
                self.props[a.name] = a

    def addPropertie(self, propertie: Arith, name=""):
        if not name:
            name = propertie.name
        assert name
        assert name not in self.props.keys()
        self.props[name] = propertie

    def addDifferential(self, diff: diffEq):
        self.differentials.append(diff)

    def __str__(self):
        txt = self.name
        for p in self.props:
            txt += "\t" + p + ": " + str(self.props[p]) + "\n"
        return txt
