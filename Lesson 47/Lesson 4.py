from pathlib import Path
# Чтение файла

with open('Lesson 2.py') as test_file:
    print(test_file.read())

with open('Lesson 2.py') as test_file:
    print(test_file.readline())

# # запись в файл
# with open('Lesson 2.py', 'w') as new_file:
#     new_file.write("First line in the new file")
#
# with open('Lesson 2.py') as new_file:
#     print(new_file.read())

# with open('Lesson 2.py', 'a') as new_file:
#     new_file.write("First line in the new file")
#
# with open('Lesson 2.py') as new_file:
#     print(new_file.read())

# удаление файлов
print(Path('new.txt').exists())
Path('new.txt').unlink()
print(Path('new.txt').exists())