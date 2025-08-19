num_one = 10
num_two = 3

if (num_one > 0 and
        num_two >0 and
        isinstance(num_one, int)
        and isinstance(num_two, int)):
    print("Both numbers are ints is positive")

my_number = 21.5

if type (my_number) is int:
    print(my_number, "is integer")
else:
    print(my_number, "is not a integer")

print()

my_phone = {
    'price': 200,
    'brand': 'Apple'
}

if my_phone.get('brand'):
    print("Phone's brand is", my_phone['brand'])
else:
    print("There is no phone brand")