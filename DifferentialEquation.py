from ArithmeticFunction import Arith

class diffEq:

    '''
    Differential Equation
    '''
    def __init__(self, target:Arith, term: Arith):
        '''
            @params:
            target - Arith Object, whose d/dt equals term
            term - Arith Object
        '''
        self.target = target
        self.term = term
        self.result = 0

    def calculate(self):
        ''' saves internally the refreshed Value of self.term'''
        self.term.refresh()
        self.result = self.term.value

    def apply(self, dt):
        ''' affects the diffEq's target with the last calulated d/dt over the time t'''
        assert len(self.target.children) == 0
        self.target.value += self.result * dt

