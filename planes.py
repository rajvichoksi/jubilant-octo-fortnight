from transport import Transport

class Plane(Transport):

    def __init__(self, miles, make):
        self.miles= miles
        self.make = make

    def takeoff(self):
        return "The plane is going up"

    def landing(self):
        return "The plane is going down"

plane_1 = Plane
print(plane_1.takeoff())