# my_set = {555, 9213, 445, 23, 30}
# my_new_set = {77}
# my_set = tuple(my_set)
# my_new_set = tuple(my_new_set)
# print(my_set.__add__(my_new_set))
# my_set = set(my_set)
# my_new_set = set(my_new_set)
# print(my_set & my_new_set)

my_set = {555, 9213, 445, 23, 30}
my_set.add(561)
set_two = {20, 7, 300, 23, 445, 561}
intersected_set = my_set.intersection(set_two)
print(intersected_set)
my_list = list(intersected_set)
print(my_list)
print(my_set)
print(set_two)