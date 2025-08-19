# Задача № 1
scores = {
    0: 'abc',
    1: 'lolo',
    2: 'fff'
}

# my_scores = {}
#
# for key in scores:
#      my_scores[key] = scores[key].upper()

my_scores = {k: v.upper() for k, v in scores.items()}
print(scores)
print(my_scores)

# Задача № 2
my_list = ['lolo', 'abc', 'Daryshya', 'Pyhpyhpyh']

my_new_list = [el for el in my_list if len(el)> 3]
print(my_new_list)
print([el for el in my_list if len(el)> 3])