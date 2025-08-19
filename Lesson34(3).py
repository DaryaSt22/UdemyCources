user_data = ['Daryshya', 89]  #В таком случае в списке должно быть точно два аргумента

def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comments"

    return f"{name} has {comments_qty} comments"

my_name, my_qty = user_data
print(my_name)
print(my_qty)

print(user_info(*user_data))
print(user_info(user_data[0], user_data[1]))
print()

my_list = [{'name': 'Dar'}, {'color': 'red'}, {'animals': 'dog'}]

my_name_one, my_color, my_animals = my_list
print(*my_list)


def my_func(name, color, animals):
    print(f"My name {name} and I have dress {color} color and I have {animals}")


result = {'name': "Daryshya", 'color': 'red', 'animals': 'dog'}

for key, value in result.items():
    print(f"{key}: {value}")



