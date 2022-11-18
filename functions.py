import sqlite3 as sq

def insert_expense(expense, cost, date):
    conn = sq.connect("expense_info.db")
    conn.execute('INSERT INTO EXPENSE_INFO (EXPENSE, COST, DATE) \
        VALUES (?, ?, ?)', (expense, cost, date))
    conn.commit()
    conn.close()

def retrieve_expense():
    results = []
    conn = sq.connect("expense_info.db")
    cursor = conn.execute("SELECT expense, cost, date FROM EXPENSE_INFO")
    for row in cursor:
        results.append(list(row))
    return results


