class Cars:
    pass
    def __init__(self, speed, model):
        self.speed = speed
        self.model = model
car1 = Cars(140, "probox")
print(car1.__dict__)
