# Проверяется включен ли один набор в другой. Теория множеств(!)
nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}

res = nums.issubset(other_nums)
print(res)
print()

my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.intersection(other_set))
print(other_set.intersection('abc'))
print(my_set.intersection('abc')) # Строки 13 и 14 вычисля.т одно и тоже
print(my_set & other_set)
print(my_set.union(other_set))  # Аналог |
print(other_set.issubset(my_set))
print(my_set.issuperset(other_set))
print(my_set.difference(other_set))
print(my_set.discard('d'))  # Удаляет нужный элемент, а еще можно использовать для удаления remove()
print(my_set.remove('abc'))
print(my_set)