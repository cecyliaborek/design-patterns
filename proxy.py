import time

class Producer:

    def produce(self):
        print('producer working hard')

    def meat(self):
        print('producer has time to meet now')


class Proxy:

    def __init__(self):
        self.occupied = False
        self.producer = None

    def produce(self):
        if not self.occupied:
            self.producer = Producer()
            time.sleep(2)
            self.producer.meat()
        else:
            time.sleep(2)
            print('producer busy')



proxy = Proxy()
proxy.produce()

proxy.occupied = True

proxy.produce()