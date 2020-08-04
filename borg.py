class Borg():
    
    _monostate = None

    def __init__(self):
        if not Borg._monostate:
            Borg._monostate = self.__dict__
            self.x = 1
        else:
            self.__dict__ = Borg._monostate

#testing how it works
A = Borg()
B = Borg()
print('A: ', A.x, 'B: ', B.x)

A.x = 2
print('A: ', A.x, 'B: ', B.x)

print('A and B the same object?: ', id(A)==id(B))