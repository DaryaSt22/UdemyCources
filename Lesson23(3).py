def merge_list_to_dict(list_one, list_two):
    return dict(zip(list_one, list_two))

merge_list_to_dict(list_one='Lala', list_two='Pyh')

print(merge_list_to_dict(list_one=['a', 'b', 'c', 'd'], list_two=['tytyt', 7893, True, 'Lala']))

res_two = merge_list_to_dict( list_one=[True, 100, {}], list_two=['abc'])
print(res_two)

res_three = merge_list_to_dict([True, 100, {}], list_two=['abc'])
print(res_three)
print("Exersice 2")

def update_car_info(**car):
    print(car)
    car['is_available'] = True
    return car


print(update_car_info(brand="Toyota", price=25000))  # В этом вызове мы указываем позиционные аргументы
# print(update_car_info("Toyota", 25000))  Возникает ошибка из-за того, что эта функция (**car)
# ожидает только аргументы с ключевыми словами из-за этого синтаксиса '(**car)' в блоке параметров.
# То есть объединяем все аргументы с ключевыми словами в один словарь. Так как написано в 22 строке
# функцию вызывать нельзя