import sqlite3

conn = sqlite3.connect('expense_info.db')
query = (''' CREATE TABLE EXPENSE_INFO
            (expense           TEXT NOT NULL,
            cost        INT NOT NULL,
            date    INT);''')
conn.execute(query)
conn.close()