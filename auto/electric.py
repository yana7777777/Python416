from auto.car import Car


class Electric(Car):
    def __init__(self, brand, model, release_year, mileage, battery_power):
        super().__init__(brand, model, release_year, mileage)
        self.battery_power = battery_power

    def info(self):
        super().info()
        print(f"Этот автомобиль имеет мощность {self.battery_power}%")


# print(__name__)

__author__ = 'Admin'

if __name__ == "__main__":
    print(f"Module {__name__} (author:{__author__})")

