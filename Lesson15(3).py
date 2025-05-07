my_cars = ['BMW', 'Mercedes']

copied_cars = my_cars
# copied_cars = my_cars.copy()  точно также как, и в 3 строке
# copied_cars = my_cars[:] точно также как, и в 3 строке

copied_cars.append('Audi')

print(copied_cars)

print(my_cars)

print(id(my_cars) == id(copied_cars))