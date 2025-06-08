# from jinja2 import Template

# name = "Игорь"
# age = 28
#
# tm = Template("Мне {{ a * 2 }} лет. Меня зовут {{ n.upper() }}.")
# msg = tm.render(n=name, a=age)
#
# print(msg)

# per = {'name': "Игорь", 'age': 28 }


# class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def get_name(self):
# #         return self.name
# #
# #     def get_age(self):
# #         return self.age
# #
# #
# # per = Person("Игорь", 28)
# #
# #
# # tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p.get_name() }}.")  #один из способов доступа при создании класса и функций
# # # tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p.name }}.")  #один из способов доступа
# # # tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p['name'] }}.")  #один из способов доступа
# # msg = tm.render(p=per)
# #
# # print(msg)


# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Сочи'},
#     {'id': 5, 'city': 'Ярославль'}
# ]
#
# link = """
# <select>
# {% for c in cities %}
#     {% if c.id > 3 %}
#         <option value="{{ c['id']}}">{{ c['city']}}</option>
#     {% elif c.city == 'Москва' %}
#         <option>{{ c['city']}}</option>
#     {% else %}
#         {{ c['city'] }}
#     {% endif %}
# {% endfor %}
# </select>
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)


# menu = [
#     {'href': '/index', 'link': 'Главная'},
#     {'href': '/news', 'link': 'Новости'},
#     {'href': '/about', 'link': 'О компании'},
#     {'href': '/shop', 'link': 'Магазин'},
#     {'href': '/contacts', 'link': 'Контакты'},
# ]
#
#
# link = """
# <ul>
#     {% for i in menu %}
#         {% if i.link == 'Главная' %}
#             <li><a href="{{ i['href'] }}" class="active">{{ i['link'] }}</a></li>
#         {% else %}
#             <li><a href="{{ i['href'] }}">{{ i['link'] }}</a></li>
#         {% endif %}
#     {% endfor %}
# </ul>
# """
#
# tm = Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)

# cars = [
#     {"model": 'Audi', 'price': 23000},
#     {"model": 'Shkoda', 'price': 17300},
#     {"model": 'Renault', 'price': 44300},
#     {"model": 'Wolksvagen', 'price': 21300},
#
# ]
#
# # tpl = "{{ (cs | max(attribute='price')).model }}"
# tpl = "{{ (cs | min(attribute='price')).model }}"
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# html = """
# {% macro set_input(name, value='', type='Text', size=10) %}
# <input type="{{ type }}" name="{{ name}}" value="{{ value }}" size="{{ size}}">
#
# {% endmacro %}
#
# <p>{{ set_input('username') }}</p>
# <p>{{ set_input('email') }}</p>
# <p>{{ set_input('password', '', 'password') }}</p>
#
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)


from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(title="Домашнее задание")

print(msg)




# persons = [
#     {'name': 'Алексей'},
#     {'name': 'Никита'},
#     {'name': 'Виталий'},
# ]
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main.html')
# msg = tm.render(users=persons, title="Домашнее задание")
#
# print(msg)


# persons = [
#     {'name': 'Николай', 'age': 50},
#     {'name': 'Андрей', 'age': 55},
#     {'name': 'Сергей', 'age': 61},
# ]
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main.html')
# msg = tm.render(title="Домашнее задание")
#
# print(msg)