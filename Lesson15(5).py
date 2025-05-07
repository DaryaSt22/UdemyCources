# Задача 1
my_list = [99, 6.5, True, 'afhg', False, 456j]
my_list.pop(2)  # удаление элемента
# del my_list[2]  тоже удаление элемента
print(my_list)
print(len(my_list))
my_list.reverse()
print(my_list)
my_new_list = [99, 'dhfbirn']
print(my_new_list)
print()
my_list.extend(my_new_list)
print(my_list)
print(my_list + my_new_list)
print()

# Задача 2
list_one = [55, 895, 12.5, 'hfogbksjrbgoerb', True]
list_two = ['Dar', 4555, 'Love', 'True and False']
print(list_one + list_two)
print(list_one.__add__(list_two))
