try:
    print(int(10/5))
# except ZeroDivisionError as e:
#     print(type(e))
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("There was nor error")
except ZeroDivisionError as e:
    print(isinstance(e, ZeroDivisionError))
    print(e)
#     print("Error - Division by Zero")
# finally:
#     print("Continue")



# try:
#     print(10/0)
# except Exception as e:  # Общий класс Exception
#     print(e)