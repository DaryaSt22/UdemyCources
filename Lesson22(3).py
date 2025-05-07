def merge_list_to_dict(list_one, list_two):
    return dict(zip(list_one, list_two))
    # return dict(zipped_seq)
    # list_one = []
    # list_two = []
    # unification = zip(list_one, list_two)
    # my_dict = dict(zip(list_one, list_two))
    # return unification, my_dict
print(merge_list_to_dict(['a', 'b', 'c', 'd'], ['tytyt', 7893, True, 'Lala']))

res_two = merge_list_to_dict(['abc'], [True, 100, {}])
print(res_two)

res_three = merge_list_to_dict([True, 100, {}], ['abc'])
print(res_three)

# print(merge_list_to_dict(565,45))