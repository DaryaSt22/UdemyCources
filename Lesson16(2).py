my_disk = {}

print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 'Toyota'
my_disk['price'] = 20000

print(my_disk)
print(id(my_disk))
print(my_disk.__doc__)
print(my_disk.items())
print(my_disk.keys())
print(list(my_disk.keys()))
print(my_disk.popitem())  # Удаляет последний добавленный ключ. Не рекомендуется его использовать.
# Не всегда знаешь, какой клю был добавлен последним. Если нужно удалить какой-то ключ,
# то лучше использовать оператор del
print()
print(my_disk)
print(my_disk.get('type'))  # Такого ключа нет в словаре, поэтому возвращается None
new_disk = my_disk.copy()
new_disk['type'] = 'ssd'
print(my_disk)
print(new_disk)
print(len(my_disk))
print(len(new_disk))
