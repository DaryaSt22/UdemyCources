my_list = [1, 2, 3]
print(id(my_list))
print(my_list)

other_list = [1, 2, 3]
other_list.append(4)
print(other_list)
print(id(other_list))

print(id([1, 2, 3]))
print()

info = {
    'name': 'Daryshya',
    'is_instructor': True
}
info_copy = info
print(info)
info['reviews'] = 5
print(info)
info_copy['reviews'] = 100
print(info_copy)

other_info = {
    'name': 'Daryshya',
    'is_instructor': True
}

new_info = {
    'name': 'Daryshya',
    'is_instructor': True,
    'reviews': []
}
print(new_info)
new_info_copy = new_info.copy()
new_info_copy['reviews'].append('Great!')
print(new_info_copy)