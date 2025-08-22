import csv

with open('test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([12346, 'Daryshya', 14631])
    writer.writerow([126, 'mike', 131])
    writer.writerow([121246, 'Dar', 11])

with open('test.csv') as csv_file:
    reader = csv.reader(csv_file)
    print(reader)
    print(type(reader))
    for line in reader:
        print(line)
    csv_list = list(reader)
    print(csv_list)