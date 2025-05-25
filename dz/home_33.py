import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(type(response.text))
todos = json.loads(response.text)
# print(type(todos[0]))
# print(todos)

todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            todos_by_user[todo["userId"]] = 1
print(todos_by_user)

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print(top_users)

max_complete = top_users[0][1]
print(max_complete)

users = []
for user, num in top_users:
    if num < max_complete:
        break
    users.append(str(user))
print(users)

max_users = " и ".join(users)
print(max_users)

print(f"Пользователи {max_users} выполнили {max_complete} задач")




# дополнительные решения
# на запись в файл csv
# with open("host.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(['hostname', 'vendor', 'model', 'location'])
#     writer.writerow(['cw1', 'Cisco', '3750', 'London'])
#     writer.writerow(['cw2', 'Cisco', '3850', 'Liverpool'])
#     writer.writerow(['cw3', 'Cisco', '3650', 'Liverpool'])
#     writer.writerow(['cw4', 'Cisco', '3650', 'London'])


# нам пришел список списков и мы его записываем в файл csv
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['cw1', 'Cisco', '3750', 'London'],
#         ['cw2', 'Cisco', '3850', 'Liverpool'],
#         ['cw3', 'Cisco', '3650', 'Liverpool'],
#         ['cw4', 'Cisco', '3650', 'London']]
#
# with open("data3.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open("data3.csv", "r") as f:
#     print(f.read())