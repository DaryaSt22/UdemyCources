import random

print(random.random())
print(random.randint(1, 10))
print(random.choice('Darya'))
print(random.choice([1, 10, 4, 8, 9, 6]))
print(random.choices([1, 10, 4, 8, 9, 6], k=4))
my_list = [1, 10, 4, 8, 9, 6]
print(random.shuffle(my_list))
print(my_list)
print()

print(''.join(random.choices('ABCD0123456789', k=8)))