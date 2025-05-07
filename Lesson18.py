# У элементов нет индексов. Получить значение по индексу в наборе нельзя,
# так как наборы не имеют строгой последовательности

post = set()
post_new = {(456, 456), 8920, 222}
# print(post[2])  # будет ошибка
#print(post.__getitem__(0))
#del post[0]
print(post)
print(post_new)

photo_size = {'190x55', '5662x322', '62'}
photo_size.add('4421x61111')
print(photo_size)
other_photo = {'62', '461347'}
all_size = photo_size|other_photo  # 16 и 17 строки вычисляют одно и тоже
all_size2 = photo_size.union(other_photo)
print(all_size)
print(all_size2)
common_s = photo_size.intersection(other_photo)  # 20 и 21 строки вычисляют одно и тоже
common_s1 = photo_size&other_photo
print(common_s)
print(common_s1)
