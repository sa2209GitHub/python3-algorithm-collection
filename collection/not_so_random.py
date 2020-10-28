# PRNG example #1

class NotSoRandom(object):
    
    def seed(self, a=3):
        self.seedval = a
        print("Random seed", self.seedval)
    
    def random(self):
        self.seedval = (self.seedval * 3) % 19
        return self.seedval


_inst = NotSoRandom()
seed = _inst.seed
random = _inst.random


seed(1234)
print([random() for _ in range(22)])

seed(1234)
print([random() for _ in range(22)])

seed(34535)
print([random() for _ in range(22)])

seed()
print([random() for _ in range(22)])