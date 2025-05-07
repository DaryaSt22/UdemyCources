my_set = {'abc', 'd', 'f', 'y', 'z'}

copied_set = my_set.copy()

my_set.add('t')
copied_set.add('l')

print(my_set.symmetric_difference(copied_set))
print((my_set | copied_set) - (my_set & copied_set))