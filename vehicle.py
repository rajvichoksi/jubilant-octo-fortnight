from transport import Transport:

class Vehicle(transport):

    def __init__(self, make, model, colour, current_speed, max_speed):
        self.make = make
        self.model = model
        self.colour = colour
        self._current_speed = current_speed
        self.max_speed = max_speed

    def get_speed(self):
        print("The car is going at: ")
        return self._current_speed

    def accelerate(self):
        print("The car has sped up to: ")
        return ((self._current_speed) + 5)

    def brake(self):
        print("The car has slowed down to: ")
        return ((self._current_speed) - 5)


car_1 = Car('Audi', 'A3', 'white', 35, 125)
car_2 = Car('BMW', 'X5', 'black', 37, 140)
