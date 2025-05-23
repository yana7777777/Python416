import json
from random import choice


def data_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'l']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel
    }

    return person, tel


def add_record(person_dict, num):
    try:
        data = json.load(open("data_person.json"))
    except FileNotFoundError:
        data = {}

    data[num] = person_dict

    with open("data_person.json", 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    add_record(data_person()[0], data_person()[1])




