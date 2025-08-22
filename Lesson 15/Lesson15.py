list_one = ['hi', True, 123]

print(len(list_one))
del(list_one[2])
print(list_one)
print(len(list_one))

# Список словарей используется очень часто. Например, когда необходимо передавать данные на сервер,
# либо с сервера. Например, загрузить список постов или список пользователей.
print()
users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 155,
        'user_name': 'Bob'
    }
]

print(len(users))
print(users[1] ['user_id'])

inputs = [True, 'hi', '10.5', 'djf']

# pop() - удаление элементов
inputs.pop()
print(inputs)

inputs.pop(0)
print(inputs)

removed_element = inputs.pop()
print(removed_element)

print(inputs)
print()

posts_ids = [245, 151, 762, 167]

posts_ids.sort()

print(posts_ids)

# reverse - объекты сортируются по убыванию
posts_ids.sort(reverse=True)

print(posts_ids)
