from zipfile import ZipFile
from pathlib import Path

with ZipFile('my_files.zip') as my_zipe_file:
    # print(my_zipe_file.infolist())
    my_zipe_file.extractall('my_files')

# print(Path.cwd())

# base = Path(__file__).parent
# zip_path = base / 'my_files.zip'
# out_dir = base / 'my_files_unzipped'
# out_dir.mkdir(parents=True, exist_ok=True)
#
# with ZipFile(zip_path) as z:
#     z.extractall(out_dir)
#
# print('Разархивировано в:', out_dir.resolve())

# Path("my_files").mkdir()

# with open("my_files/first.txt", "w") as my_file:
#     my_file.write("This is firth file!")
#
# with open("my_files/second.txt", "w") as my_file:
#     my_file.write("This is second file!")
#
# with ZipFile('my_files.zip', mode='w') as my_zip_file:
#     print(my_zip_file)
#     for file in Path('my_files').iterdir():
#         print(file)


