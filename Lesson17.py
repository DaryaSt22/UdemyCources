# Кортеж изменять нельзя. Именно круглые скобки являются индекатором, что это кортеж.
# Порядок следования элементов в кортежах важен. И удалять элементы также нельзя.

my_fruits = 'banana'
other_fruits = 'lime'
all_fruits = (my_fruits, other_fruits)
print(all_fruits)
print()
print(len(my_fruits))
print(len(other_fruits))
print(my_fruits[0])
# my_fruits[2] = 'apple'
# print(my_fruits) # - будет возникать ошибка, так как кортежи неизменяемые

users = (
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
)

print(users[1]['user_id'])
users[1]['user_id'] = 100  # Изменяемые объекты в кортежах можно изменять

print(users[1]['user_id'])

iternal_one = (456, 8953, 5555666)
iternal_two = (77, 99, 125)
print(iternal_one + iternal_two)