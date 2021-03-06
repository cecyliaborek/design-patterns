import types

class Strategy:

    def __init__(self, function=None):
        self.name = 'Default strategy'
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        print(f'{self.name} is used')


def strategy_one(self):
    print(f'{self.name} is used to execute method 1')

def strategy_two(self):
    print(f'{self.name} is used to execute method 2')


def_strategy = Strategy()
def_strategy.execute()

strategy1 = Strategy(strategy_one)
strategy1.name = 'strategy one'
strategy1.execute()

strategy2 = Strategy(strategy_two)
strategy2.name = 'strategy two'
strategy2.execute()