# Унарные операторы всегда имеют один операнд

my_num = 10

print(not my_num)

my_bool = True
print(+ my_bool)

# У бинарных операторов всегда два операнда
# Инфиксная запись - это когда оператор находится между операндами. Например:
# a = True
print("Задача")


set_one = {12, 456, 51, 88}
set_two = {22, 456, 792, 792}
print(set_one is set_two)
print(set_one.__eq__(set_two))
print(set_one == set_two)
print(12 in set_one)
print()


print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(None))
print(bool([]))
print(bool({}))
print(bool(""))
print(not not [00])
print()

my_list = [1, 2]

if len(my_list) > 0:
    print("Elements")


my_list = [1, 2]

if my_list:
    print("Elements")

# def fac(n):
#     return n * fac(n-1)
#
#
# print(fac(n=3))

counter = 1
for i in(1, 2, 3):
    counter += 1

print(counter)
print()

x = 2
y = 1
x *= y + 1

print(x)

print()
my_list = [1, 5, 5, 5, 5, 1]
max_ = my_list[0]
index_of_max = 0
for i in range(1, len(my_list)):
    if my_list[i] > max_:
        max_ = my_list[i]
        index_of_max = i

print(index_of_max)
