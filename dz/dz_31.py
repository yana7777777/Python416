from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, brand, model, release_year, mileage):
        self.brand = brand
        self.model = model
        self.release_year = release_year
        self.mileage = mileage

    @abstractmethod
    def info(self):
        print(f"\n{self.brand}, {self.model}, {self.release_year} год, {self.mileage} км")


class Electric(Car):
    def __init__(self, brand, model, release_year, mileage, battery_power):
        super().__init__(brand, model, release_year, mileage)
        self.battery_power = battery_power

    def info(self):
        super().info()
        print(f"Этот автомобиль имеет мощность {self.battery_power}%")


class Haval(Car):
    def __init__(self, brand, model, release_year, mileage, awd):
        super().__init__(brand, model, release_year, mileage)
        self.awd = awd

    def info(self):
        super().info()
        print(f"Этот автомобиль имеет привод {self.awd}")


el1 = Electric("Тесла", "T", "2018", 99000, 100)
el2 = Electric("Li Auto", "LiXiang MEGA", "2024",20000, 100)

hl1 = Haval("Haval", "Chitu", "2021", 27000, "4WD")
hl2 = Haval("Haval", "Dargo", "2024", 7000, "4WD")

car = [el1, el2, hl1, hl2]

for car in car:
    car.info()


