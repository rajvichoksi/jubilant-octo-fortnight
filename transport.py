class Transport:

    def __init__(self, type, seats, wheels, location):
        self.type = type
        self.seats = int
        self.wheels = int
        self.location = location

    def accelerate(self):
        return "The " + self.type + " is moving forward"

    def brake(self):
        return "The " + self.type +  " is slowing down"

    def wheels(self):
        return "This vehicle has " + self.wheels

plane = Transport( 'plane', 800, 16, 'air')
boat = Transport('boat', 300, 0, 'water')
train = Transport('train', 150, 56, 'land')
vehicle = Transport('vehicle', 5,4, 'land')

print(plane.accelerate())
print(train.brake())


