import re
from re import search

my_string = 'My name is Daryshya. Daryshya'

print(re.search('D......a', my_string))
print(re.search('^M.*name', my_string))
print(re.search('D......a.$', my_string))
print(r'D......a.$')
res = re.search('D......a.$', my_string)
print(res.span())
print()

#  my_pattern = re.compile(r'^My.*\.$')
my_pattern = re.compile(r'D......a')
print(my_pattern)
print(my_pattern.search(my_string))
print(my_pattern.match(my_string))
print(my_pattern.findall(my_string))
