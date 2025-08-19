# my_dict = {
#     'image_id': 142,
#     'image_title': 'PyhPyhPyyyhhh'
# }
#
# def image_info(my_dict):
#     if my_dict in image_id ==142:
#         Tru
# TypeError:
#     print("No values")



def image_info(img):
    if ('image_id' not in img) or ('image_title' not in img):
        raise TypeError("Keys image_id and image_title must be present")
    return f"Image '{img['image_title']}' has id {img['image_id']}"

print(image_info({'image_title' : "My dog", 'image_id' : 1254}))
try:
    print(image_info({'image_title': "My dog"}))
except TypeError as e:
    print("You have wrong!")
    print(e)


