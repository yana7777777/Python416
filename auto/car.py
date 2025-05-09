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

