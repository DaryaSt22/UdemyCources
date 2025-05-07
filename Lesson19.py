my_range = range(2)

my_list = []

for n in range(10, 30, 2):
    my_list.append(n)
    print(n)

print(my_list)
print()
print(list(range(12, 25, 2)))
print(tuple(range(12, 25, 2)))
print(set(range(12, 25, 2)))

my_range = range(10, 30, 3)
print(dir(my_range))
print(my_range.stop)
print(my_range.index(19))
print(my_range.count(10))