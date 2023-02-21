from ArithmeticFunction import Arith

class diffEq:
    def __init__(self, target:Arith, term: Arith):
        self.target = target
        self.term = term
        self.result = 0

    def calculate(self):
        self.term.refresh()
        self.result = self.term.value

    def apply(self, dt):
        assert len(self.target.children) == 0
        self.target.value += self.result * dt

