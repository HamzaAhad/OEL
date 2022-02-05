import sqlite3

conn = sqlite3.connect("member.db")
#create a cursor
cursor = conn.cursor()

#create a Table

cursor.execute("""CREATE TABLE members(
   member_id INTEGER PRIMARY KEY,
   member_name,
   check_out,
   reserved
)""")



#NULL INT REAL TEXT BLOB
#commit our command
conn.commit()
#close our connection
conn.close()