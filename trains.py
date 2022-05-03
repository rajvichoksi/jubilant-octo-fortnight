from transport import Transport

class Train(Transport):

    def __init__(self, carriages, company):
        self.carriages = carriages
        self.company = company

    def noise(self):
        return "choo choo!"

train_1 = (8, "Network Rail")
print(Train.noise())


