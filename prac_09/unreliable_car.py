import random
from car import Car  # 假设您的 Car 类定义在 car.py 文件中


class UnreliableCar(Car):


    def __init__(self, name="", fuel=0, reliability=70.0):

        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):

        if random.uniform(0, 100) < self.reliability:
            driven_distance = super().drive(distance)
        else:
            driven_distance = 0
        return driven_distance
