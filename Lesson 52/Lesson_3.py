import re

email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"

email_check_pattern = re.compile(email_regexp)

def check_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)
    validation_result = "valid" if email_check_pattern.fullmatch(email) else "not valid"
    return (email, validation_result)


print(check_email('ds@gmail.com'))
print(check_email('ds@gil.com'))
print(check_email('d@gmaicom'))