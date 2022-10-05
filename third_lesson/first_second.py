class Car:
    def __init__(self, capacity, speed, number):
        self.capacity = capacity
        self.speed = speed
        self.number = number


class RaceCar(Car):
    def __init__(self, speed, capacity, number):
        super().__init__(speed)
        self.capacity = 0
        self.number = None
        self.speed = speed


c = Car(1000, 100, "a720po")
print(c.capacity, c.speed, c.number)
r = RaceCar(300)
print(r.capacity, r.speed, r.number)