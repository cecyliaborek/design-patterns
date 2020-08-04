class Singleton():

    _single = None

    def __init__(self):
        if not Singleton._single:
            self.x = 1
        else:
            raise RuntimeError('Singleton already exists')
    
    @classmethod
    def get_instance(cls):
        if not cls._single:
            cls._single = Singleton()
        return cls._single


#testing how it works
a = Singleton.get_instance()
b = Singleton.get_instance()
print('a: ', a.x, 'b: ', b.x)

a.x = 2
print('a: ', a.x, 'b: ', b.x)

print('a and b the same object?: ', id(a)==id(b))