# import random
#
# random_num = random.randint(1,5)
# while True:
#     num = int(input("Guess the number from 1 to 5: "))
#     if num != random_num:
#         print("Try again!")
#         continue
#     print("Congratulations!", random_num)
#     break


# Задача
while True:
    num_one = float(input("Write your number: "))
    num_two = float(input("Write your number: "))
    print(num_one / num_two)
    answer= input("Do you want to continue? (Yes/No): ")
    if answer == 'Yes':
        continue
    if answer == 'No':
        break