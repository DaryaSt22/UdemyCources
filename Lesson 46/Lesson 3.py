import json

my_dict = '{"Name": "Daryshya", "Status": "happy", "Age": 21}'

sneakers = json.loads(my_dict)

my_sneakers = json.dumps(my_dict, indent=2)
print(my_sneakers)
print(sneakers)
print(type(my_dict))
print(type(my_sneakers))
print()

dict_my = {
    'a': 2,
    'b': {
        'c': [1, 2, 3]
    },
    'd': (1, 2, 3)
}

converted_dict = json.dumps(dict_my)
print(converted_dict)
print(type(converted_dict))

converted_json = json.loads(converted_dict)
print(converted_json)