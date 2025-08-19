my_fruits = ['apple', 'banana', 'lime']

# my_apple, my_banana, my_lime = my_fruits
my_apple, *remaining_fruits = my_fruits

print(my_apple)
print(remaining_fruits)
# print(my_banana)
# print(my_lime)
print()

my_list = [1, 2, 3]

first, second, third = my_list

print(first)
print(second)
print(third)
print()


my_fruits_tuple = ('apple', 'banana', 'lime')

you_apple, you_banana, you_lime = my_fruits_tuple

print(you_apple)
print(you_banana)
print(you_lime)
