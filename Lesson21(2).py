from copy import deepcopy

info = {
    'name': 'Daryshya',
    'is_instructor': True,
    'reviews': []
}

info_deepcopy = deepcopy(info)
info_deepcopy['reviews'].append('Great!')
print(info)

print(info_deepcopy)