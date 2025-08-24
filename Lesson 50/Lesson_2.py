from datetime import datetime, timedelta

my_datetime = datetime(2222, 12, 10, 5, 10, 14)
print(my_datetime + timedelta(days=100, minutes=120))
print(my_datetime - timedelta(days=100, minutes=120))