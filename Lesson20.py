fruits = ['apple', 'banana', 'lime']

quantities = [100, 70, 50]
# quantities = '1563'
# availability = [True, True, False, True]

# fruit_qtys_zip = zip(fruits, quantities)
# print(fruit_qtys_zip)
#
# fruit_qtys_dict = dict(fruit_qtys_zip)
# print(fruit_qtys_dict)

merch = ['T-shirt', 'trousers', 'jacket']
price = [456, 128, 2000]

unification = zip(merch, price)
print(list(unification))
my_dict = dict(zip(merch, price))
print(my_dict)
