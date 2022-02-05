import sqlite3

conn = sqlite3.connect("book.db")
#create a cursor
cursor = conn.cursor()

#create a Table
# cursor.execute("""CREATE TABLE books(id INTEGER AUTOINCREMENT,
#     title TEXT,
#     author TEXT,
#     sub TEXT,
#     pub_date TEXT
    
# )""")
cursor.execute("""CREATE TABLE books (
   book_id INTEGER PRIMARY KEY,
   title TEXT NOT NULL,
   author TEXT NOT NULL,
   sub TEXT NOT NULL,
   pub_date TEXT NOT NULL,
   check_out,
   reserved
)""")

#cursor.execute("CREATE TABLE customers(first_name DATATYPE,last_name DATATYPE,email DATATYPE)")

#NULL INT REAL TEXT BLOB
#commit our command
conn.commit()
#close our connection
conn.close()