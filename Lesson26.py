def print_number_info(num):
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")
    return num

print_number_info(2)
print("Пример 2 ")

a = 10
b = True

def my_fn():
    global b
    a = True
    b = 15
    print(a)
    return b


my_fn()


print(a)
print(b)
print("Пример 3")


c = 5
def my_fn_new(m, n):
    print(m, n)
    print(c)


my_fn_new('abc', 'xyz')
print(dir())
