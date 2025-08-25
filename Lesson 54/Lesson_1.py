import sqlite3

DB_NAME = "sqlite_db.db"

with sqlite3.connect(DB_NAME) as sqlite_connection:
    sqlite_request = "SELECT * FROM courses WHERE reviews_qty>=30"
    sql_cursor = sqlite_connection.execute(sqlite_request)
    # for record in sql_cursor:
    #     print(record)
    records = sql_cursor.fetchall()
    print(records)


# Запись данных в таблицу
# Add records to the courses table
# courses = [
#     (351, "JavaScript course", 25, 5),
#     (155, "PHP course", 40, 10),
#     (358, "C++ course", 62, 33)
# ]
#
# with sqlite3.connect(DB_NAME) as sqlite_connection:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     for course in courses:
#         sqlite_connection.execute(sql_request, course)
#     # sqlite_connection.execute(sql_request, (255, "Python course", 25, 15))
#     sqlite_connection.commit()


# with sqlite3.connect(DB_NAME) as sqlite_connection:
#     print(sqlite_connection)
#     print(sqlite3.sqlite_version)

# Create new table
# with sqlite3.connect(DB_NAME) as sqlite_connection:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );"""
#     sqlite_connection.execute(sql_request)