import copy

class Prototype():
    
    def __init__(self):
        self._objects = {}

    def register_object(self, name, object_):
        self._objects[name] = object_

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car():

    def __init__(self):
        self.name = "panda"
        self.color = "yellow"

    def __str__(self):
        return f'{self.name}|{self.color}'



panda = Car()
prototype = Prototype()

prototype.register_object('panda', panda)
panda2 = prototype.clone('panda')

print(panda)
print(panda2)