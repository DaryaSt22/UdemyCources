from pathlib import Path


file_path = Path('test.txt')
print([m for m in dir(file_path) if not m.startswith('_')])

print(Path.cwd()) # текущая директория

# формирование путей
print(Path('C:/').joinpath('Users').joinpath('Darya'))
print(Path('C:/') / 'Users' / 'Darya')

# проверка присутствия файла или директории
print(Path('main.py').exists())
print(Path('test.txt').exists())
print()
# директория или файл?
print(Path('test.txt').is_file())
print(Path('test.txt').is_dir())
print()

# список файлов и папок
for f in Path('.').iterdir():
    print(f)