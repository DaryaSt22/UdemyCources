from sys import getsizeof

# nums = [3, 5, 10]
#
# gen = (num * num for num in nums)
#
# squares = tuple(gen)
#
# print(squares)
# print(type(squares))

squares_gen = (num * num for num in range(100_000_000))
print(getsizeof(squares_gen))
print(type(squares_gen))

for elem in squares_gen:
    print(elem)
    if elem == 100:
        break

squares_list = [num * num for num in range(100)]
print(getsizeof(squares_list))
print(type(squares_list))