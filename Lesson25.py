def other_fn():
    pass


def fn_with_callback(callback_fn):
    callback_fn


fn_with_callback(other_fn())
print("Пример 2")


def print_number_info(num):
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")


def print_square_num(num):
    print("Square of the num is ", num * num)


def process_number(num, callback_fn):
    callback_fn(num)


entered_num = int(input("Enter any number: "))

process_number(entered_num, print_number_info)
process_number(entered_num, print_square_num)
print("Пример 3 ")


def send_data(data):
    pass


def process_data(input_data, send_data_fn):
    updated_data = input_data.copy()
    send_data_fn(updated_data)


print(process_data({'name': 'Daryshya'}, send_data))