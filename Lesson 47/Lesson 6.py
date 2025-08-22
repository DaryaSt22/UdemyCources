from pathlib import Path

# Создание папки
files_dir_path = Path('files')
files_dir_path.mkdir(exist_ok=True)

with open('files/first.txt', 'w') as test_file:
    test_file.write("First string!\n")
    test_file.write("Second string!\n")

with open('files/second.txt', 'w') as test_file:
    lines = [
        "First line!"
        "Second line"
        "Last line!"
    ]
    for line in lines:
        test_file.write(line + '\n')
    # test_file.write("First string!\n")
    # test_file.write("Second string!\n")

with open('files/first.txt') as test_file:
    print(test_file.read())

with open('files/second.txt') as test_file:
    print(test_file.read())

# удаление файлов
# Path('files/first.txt').unlink()
# Path('files/second.txt').unlink()

# удаление папки
# files_dir_path.rmdir()