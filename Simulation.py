import numpy as np
from PhysicalBody import Body

class Simulation:

    def __init__(self, bodys:list[Body], type: str, dt: float, n: int):
        self.bodys = bodys
        self.type = type
        self.dt = dt
        self.n = n
        self.time = np.linspace(0, dt * n, n)
        self.plotBodys = {}
        for b in self.bodys:
            assert b.name not in self.plotBodys.keys()
            self.plotBodys[b.name] = {}
            for p in b.props:
                self.plotBodys[b.name][p] = np.zeros(self.n)