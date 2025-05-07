my_motorbike = {
    'brand': 'Honda',
    'price': 2000,
    'engine_vol': 1.2,
    'price_info': {  # Значением может быть другой словарь
        'price': 25000,
        'is_available': True
    }
}

print(my_motorbike['price_info']['price'])
# print(dir(my_motorbike))  # Проверяем какие есть атрибуты у объекта my_motorbike
my_motorbike['brand'] = 'Hoho'
print(my_motorbike)
print(my_motorbike['brand'])  # Получаем доступ к значениям тех или иных ключей
print(my_motorbike['price'])
my_motorbike['car'] = 'Blue'
print(my_motorbike)
del my_motorbike['car']  # Удаление элементов (ключа и значение, то есть удаляет всю строку)
print(my_motorbike)

key_name = 'brand'  # Доступ к значению элемента с помощью переменной
my_motorbike[key_name] = 'BMW'
print(my_motorbike)


brand_two = 'BMW'
car_price = 23000
engine_volume_two = 1.2

my_car = {
    'brand': brand_two,
    'price': car_price,
    'volume': engine_volume_two,
}

print(my_car)
print(len(my_car))
print()
print(my_car.get('menu'))  # Метод get() для получения значений ключей и ошибки ключа не возникнет
print(my_car.get('gty', 55))  # Если такого ключа нет, то метод get() вернет значение 0
print(my_car.get('brand'))
print(my_car.__doc__)