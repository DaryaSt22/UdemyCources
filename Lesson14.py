int_num = 50
float_num = 7.5
str_val = "abc"

print(int_num * float_num)
print(int_num * str_val)
print(int_num.__mul__(float_num))
print(float_num.__rmul__(int_num))