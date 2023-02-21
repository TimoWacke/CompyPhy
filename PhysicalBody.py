from ArithmeticFunction import Arith
from DifferentialEquation import diffEq
import numpy as np


class Body:
    '''
    Physical Object, that owns passed properties in form of Arith Objects.
    Properties can be passed on creation as list,
    or later added with addProperty()

    it can also save differnetial Equations (Objects of diffEq Class), with these
    you can have all what you need to calculate the properties changes over time right at hand if wished.
    '''

    params = []
    units = []
    timeUnit = ''

    def __init__(self, name:str, properties: list[Arith] = []):
        '''
        @params
            name - str: requiered
            properties - list: not requiered
        '''
        self.name = name
        self.props = {}
        self.differentials = [] #diffEq's
        usednames = []
        for a in properties:
            if a.name:
                assert a.name not in usednames
                usednames.append(a.name)
                self.props[a.name] = a

    def addProperty(self, propertie: Arith, name=""):
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
