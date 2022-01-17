import sqlite3
conn = sqlite3.connect('Users details.db')
c = conn.cursor()
c.execute("select * from user_data")
for i in c:
	print(i)