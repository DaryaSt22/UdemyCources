my_nums = [10, 5, 0, 44, 5, 85]

print(type(my_nums))
print(dir(my_nums))

print(my_nums.count(5))

my_nums.append(25)
print(my_nums)

my_nums.insert(2, -5)
print(my_nums)

# my_nums.clear()
# print(my_nums)

my_nums.extend('abc')
print(my_nums)

other_nums = my_nums.copy()
print(id(my_nums))
print(id(other_nums))

my_nums.append(5)
other_nums.clear()

print(my_nums, other_nums)

print(len(my_nums))