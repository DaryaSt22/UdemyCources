for el in ['abc', 123, True]:
    print(type(el))
    print(el)

print(el)
print()

my_dict = {'id': 123}
for key in my_dict:
    print(key)
    print(my_dict[key])
print()

my_object = {
    'x': 10,
    'y': True
}

for item in my_object.items():
    key, value = item
    print(key,value)

for key, value in my_object.items():
    print(key, value)

print()

for i in range(10):
    print(i)
print()

for i in range(2, 20, 2):
    print(i)
print()


# Задача №1
def dict_to_list(dict_to_convert):
    list_for_convertion = []
    for k, v in dict_to_convert.items():
        if type(v) == int:
            v *= 2
        list_for_convertion.append((k, v))
    return list_for_convertion

print(dict_to_list({'a':20, 'b':199}))
print()


# Задача №2
# def filter_list(list_to_filter, value_type):
#     filtered_list = []
#     for element in list_to_filter:
#         if isinstance(element, str):
#             filtered_list.append(element)
#         # if type(element) == value_type:
#         #     filtered_list.append(element)
#     return filtered_list
#
# print(filter_list([35, True, 'abc', 10], int))
# print(filter_list([35, True, 'abc', 10], str))
# print(filter_list([35, True, 'abc', 10], bool))


# Второй вариант решения задачи №2
def filter_list(list_to_filter, value_type):
    # def check_element(elem):
    #     return type(elem) is value_type
        # return isinstance(elem, value_type)
    #return list(filter(check_element, list_to_filter))
    return list(filter(lambda elem: type(elem) is value_type, list_to_filter))

print(filter_list([1, 10, 5.5, 'abc'], int))
