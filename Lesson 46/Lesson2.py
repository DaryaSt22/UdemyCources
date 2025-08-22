import json


json_str = '{"id": 235, "brand": "Nike", "qty":84, "status": {"isForSale": true}}'
json_array = '[1, 2, 3]'

sneakers = json.loads(json_str)

print(type(sneakers))

print(sneakers['brand'])
print(sneakers['id'])

print(json.dumps(sneakers, indent=1))
print(json.loads(json_array))

json_from_dict = json.dumps(sneakers, indent=1)
print(json_from_dict)
print()
print(type(json_from_dict))

