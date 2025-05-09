from auto.car import Car


class Haval(Car):
    def __init__(self, brand, model, release_year, mileage, awd):
        super().__init__(brand, model, release_year, mileage)
        self.awd = awd

    def info(self):
        super().info()
        print(f"Этот автомобиль имеет привод {self.awd}")


