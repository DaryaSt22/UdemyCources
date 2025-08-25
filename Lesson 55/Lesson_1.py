from array import array

my_int_array = array("i", [1, 4, 6, 10, 5, 9, 5, 6, 5])

# print(my_int_array)
# print(type(my_int_array))
#
# my_int_array.append(15)
# print(my_int_array)

# print(my_int_array.count(5))
# my_int_array.pop()  # удаляет последний элемент массива
# print(my_int_array)
# print(len(my_int_array))
# print()
#
# for elem in my_int_array:
#     print(elem)

with open('my_array.bin', 'wb') as my_file:
    my_int_array.tofile(my_file)

imported_array = array("i")

with open('my_array.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 3)
    print(imported_array)

imported_array.reverse()
print(imported_array)
