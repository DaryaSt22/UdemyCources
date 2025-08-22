from os import path
from pathlib import Path

print(path.curdir)
print(path.abspath('.'))
print()

print(type(Path))

cwd = Path('.')
print(cwd)
print()
print(isinstance(cwd, Path))
print(type(cwd))
print()
print(Path.__subclasses__())
print(dir(cwd))
print()
print(cwd.absolute())