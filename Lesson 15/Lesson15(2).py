greeting = "Hello from Python"
greeting_letters = list(greeting)

print(greeting_letters)
print()

my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)

print(my_dict_keys)
print()

rattings = [2.5, 5.0, 4.3, 3.7]

print(min(rattings))
print(max(rattings))
print(sum(rattings))
print(sum(rattings)/len(rattings))
print()

my_ratting = [2.5, 5.0]
other_rattings = [3.7, 4.5, 4.9]
all_rattings = my_ratting + other_rattings
print(all_rattings)
print()

rattings_two = [2.5, 5.0, 4.3, 3.7, 8.8, 2,6]
first_two_rattings = rattings_two[:2]
print(first_two_rattings)

middle_rattings = rattings_two[1:-1]
print(middle_rattings)

last_two_rattings = rattings_two[-2:]
print(last_two_rattings)

