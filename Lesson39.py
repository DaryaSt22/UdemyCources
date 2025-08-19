all_nums = [-3, 1, 0, 10, -20, 5]

# absolute_nums = []

absolute_nums = [abs(num) for num in all_nums]

# for num in all_nums:
#     absolute_nums.append(abs(num))

print(absolute_nums)
print(all_nums)


# positive_nums = []
# for num in all_nums:
#     if num > 0:
#         positive_nums.append(num)
positive_nums = [num for num in all_nums if num > 0]

print(positive_nums)
print(all_nums)

