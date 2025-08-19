# route_info = {
#     'distance': 200,
#     'speed': 180,
#     'time': 2
# }
#
# if route_info.get('distance'):
#     distance = route_info['distance']
#     print(f"Distance to your destination is {distance}")
# elif

# elif a >= b:
#     info = f"{a} больше или равно {b}"
# else:
#     info = f"{a} меньше {b}"
# return info



def route_info(route):
    if ('distance' in route) and (type(route['distance']) == int):
        return f"Distance to you destination is {route['distance']}"
    if ('speed' in route) and ('time' in route):
        return f"Distance to you destination is {route['speed'] * route['time']}"

    return f"No distance info is available"

print(route_info({'distance': 15}))
print((route_info({'speed': 20, 'time': 3})))
print((route_info({'my_speed': 14})))
