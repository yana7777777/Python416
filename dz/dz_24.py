class Car:
    model = "model"
    year = "year"
    fabricator = "fabricator"
    power = "power"
    color = "color"
    price = "price"

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}\nГод выпуска: {self.year}\n"
              f"Производитель: {self.fabricator}\nМощность двигателя: {self.power}\n"
              f"Цвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def input_info(self, model, year, fabricator, power, color, price):
        self.model = model
        self.year = year
        self.fabricator = fabricator
        self.power = power
        self.color = color
        self.price = price

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color


c1 = Car()
c1.input_info("X7 M50i", "2021", "BMW", "530 л.с.", "white", "1079000")
c1.print_info()
c1.set_color("blue")
c1.print_info()
print(c1.get_color())





