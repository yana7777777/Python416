# import json
#
# data = {'name': 'Yana',
#         'age': 54,
#         'live': 'Samara'}
#
# with open("data_file.json", "w") as f:
#     json.dump(data, f, indent=4)
#
# with open("data_file.json", "r") as f:
#     data1 = json.load(f)
#
# print(data1)
#
# string = json.dumps(data, sort_keys=True)
# print(string, type(string)) # работать со строкой как со словарем мы  не можем
#
# data1 = json.loads(string) # преобразуем в словарь
# print(data1, type(data1))