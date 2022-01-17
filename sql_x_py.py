import sqlite3
conn = sqlite3.connect('password.db')
c = conn.cursor()

# creating table
# c.execute('''CREATE TABLE stock
# 	(date text, trans text, symbol text, qty real, price real)''')
# Inserting a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")
#save and commit the changes
conn.commit()
c.execute("SELECT * from stocks")
print(c.fetchone())

