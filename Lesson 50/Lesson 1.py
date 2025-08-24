from datetime import date, time, datetime

my_date = date(2100, 4, 15)
print(my_date)
print(my_date.day)
print(my_date.today())

print(my_date.isocalendar())
print()

my_time = time(18, 10, 45)
print(my_time)

print(my_time.hour)
print(my_time.minute)
print(my_time.fold)
print()
my_datetime = datetime(2222, 12, 2, 5, 10, 14)
print(my_datetime)
print(my_datetime.year)
print(my_datetime.isoformat())
print(my_datetime.now())
print()
print(my_datetime.strftime('%d-%b-%Y'))
print(my_datetime.strftime('%d-%m-%Y %H:%M:%S'))

date_str = '02-12-2222'
converted_date = datetime.strptime(date_str, format('%d-%m-%Y'))
print(converted_date)