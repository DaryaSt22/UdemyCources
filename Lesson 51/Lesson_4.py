import math

def cal_factorial(num):
    if type(num) is not int:
        raise TypeError("Number must be integer!")
    if num <= 0:
        raise ValueError("Number must be positive!")
    if num == 1:
        return 1
    return cal_factorial(num - 1) * num

print(cal_factorial(15))
print(math.factorial(10))