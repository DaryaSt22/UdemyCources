my_set = {1, 10, 15}

# new_set = set()
new_set = {val * val for val in my_set}

# for val in my_set:
#     new_set.add(val * val)

print(new_set)
print(my_set)

# my_scores = {
#     'a': 10,
#     'b': 7,
#     'm': 14
# }
my_scores = [10, 7, 14]
# scores = {}

# scores = {k: v for k, v in enumerate(my_scores)}
scores = {index: elem for index, elem in enumerate(my_scores)}

# scores = {k: v * 10 for k, v in my_scores.items()}
# scores2 = {v * 10 for k, v in my_scores.items()}

# for key, value in my_scores.items():
#     scores[key] = value * 10

print(scores)
# print(scores2)
print(my_scores)