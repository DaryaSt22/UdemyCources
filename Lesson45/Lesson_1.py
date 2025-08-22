from Lesson45 import Lesson_1_2 as Les # переименовала файл
from Lesson45.Lesson_1_2 import * # my_name # or *

print(dir(Les))
print(Les.print_sum(55, 55))
print(my_name)

print(dir())
print(__name__)
print(__name__ == '__main__')
