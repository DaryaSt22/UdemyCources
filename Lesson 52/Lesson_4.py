import re
import string

def check_password(password):
    # len_regexp = r"\S{8,}"
    # lengh_pattern = re.compile(len_regexp)
    length_pattern = re.compile(r"\S{8,}")
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    number_pattern = re.compile(r"^.*[0-9]+.*$")
    special_symbol_pattern = re.compile(r"^.*[@#$%^&*()_+]+.*$")
    no_whitespace_pattern = re.compile(r"^\S*$")

    if not re.fullmatch(no_whitespace_pattern, password):
        return False, "No whitespaces allowed in the password"
    if not re.fullmatch(length_pattern, password):
        return False, "Password must have at least 8 symbols"
    if not re.fullmatch(lowercase_pattern, password):
        return False, "Password must have at least one lowercase letters"
    if not re.fullmatch(uppercase_pattern, password):
        return False, "Password must have at least one uppercase letters"
    if not re.fullmatch(number_pattern, password):
        return False, "Password must have at least one number"
    if not re.fullmatch(special_symbol_pattern, password):
        return False, "Password must have at least one special symbol @#$%^&*()_+"
    return True, "Password is valid"


# print(check_password('k^^$$)136D'))
# print(check_password('36D'))
# print(check_password('k^136D'))
# print(check_password('^^$DDFVDVGBdvrgre$)136D'))
# print(check_password('DDFdffs    Bdvrgre$   )136D'))
# print(check_password('BdvrgreW$   )136D'))

while True:
    password = input("Please enter password: ")
    password_result = check_password(password)
    if password_result[0]:
        print(password_result[1])
        break
    print(password_result[1])














# def check_password(password):
#     check_my_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
#     password_check_pattern = re.compile(check_my_password)
#     validation_result = "valid" if password_check_pattern.fullmatch(password) else "not valid"
#     return (password, validation_result)
#
# print("Enter password: ")
# test_password = str(input())
#
# if len(test_password) < 8:
#     print("Invallid password")
# if test_password == string.ascii_lowercase:
#     print("Correct!")