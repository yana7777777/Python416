# import auto.electric
# import auto.haval

# from auto import *

from auto import electric, haval


def ran():
    el1 = electric.Electric("Тесла", "T", "2018", 99000, 100)
    el2 = electric.Electric("Li Auto", "LiXiang MEGA", "2024",20000, 100)

    hl1 = haval.Haval("Haval", "Chitu", "2021", 27000, "4WD")
    hl2 = haval.Haval("Haval", "Dargo", "2024", 7000, "4WD")

    car = [el1, el2, hl1, hl2]

    for car in car:
        car.info()


if __name__ == "__main__":
    ran()

