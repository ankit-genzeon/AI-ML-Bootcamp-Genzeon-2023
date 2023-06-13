import sqlite3

'Bootcamp2023.db'
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)

query = ''' delete from participants'''
conn.execute(query)

print(conn.total_changes)
conn.rollback()
