from pathlib import Path

# test_file = open('test.txt', 'w')
#
# # print(test_file)
# # print(type(test_file))
#
# test_file.write("First string!\n")
# test_file.write("Second string!\n")
#
# test_file.close()

with open('test.txt', 'w') as test_file:  # при использовании with метод close() вызовится автоматически
    # и закрывать файл не нужно
    test_file.write("First string!\n")
    test_file.write("Second string!\n")
    test_file.write("Third string!\n")

# test_file = open('test.txt')
#
# print(test_file.read())
# test_file.close()

with open('test.txt') as test_file:
    # print(test_file.readlines()) # более корректный код при использовании with
    # lines = test_file.readlines()  # итерация по линиям в файле
    for line in test_file:
        # for line in lines:
        print(line)

with open('test.txt') as test_file:
    while True:
        line = test_file.readline()
        print(line)
        if not line:
            break

# Path('test.txt').unlink() # удаление файла
