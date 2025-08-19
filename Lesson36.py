my_img = ('1920', '1080')

print(f"{my_img[0]} * {my_img[1]}") if len(
    my_img) == 2 else print(f"Incorrect image formatting")


info = (f"{my_img[0]} * {my_img[1]}") if len(
    my_img) == 2 else (f"Incorrect image formatting")

print(info)

if len(my_img) == 2:
    print(f"{my_img[0]} * {my_img[1]}")
else:
    print(f"Incorrect image formatting")

if len((my_img)) > 79:
    print(f"Sring ig long")
else:
    print(f"String is short")

print("String is long" if len(my_img) > 79 else "String is short")



