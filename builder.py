class Car():
    def __init__(self):
        self.model = None
        self.engine = None
        self.tires = None

    def __str__(self):
        return f'{self.model}|{self.engine}|{self.tires}'


class Builder():
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class PandaBuilder(Builder):
    def add_model(self):
        self.car.model = 'Panda'

    def add_tires(self):
        self.car.tires = 'Kenda'

    def add_engine(self):
        self.car.engine = 'Turbo 2g'

class AudiBuilder(Builder):
    def add_model(self):
        self.car.model = 'A4'

    def add_tires(self):
        self.car.tires = 'Michellin'

    def add_engine(self):
        self.car.engine = '4k'

class Director():
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.create_new_car()
        self.builder.add_model()
        self.builder.add_tires()
        self.builder.add_engine()

    def get_car(self):
        return self.builder.car



builder = PandaBuilder()
director = Director(builder)
director.construct_car()

panda = director.get_car()
print(panda)

audi_builder = AudiBuilder()
director = Director(audi_builder)
director.construct_car()
audi = director.get_car()
print(audi)