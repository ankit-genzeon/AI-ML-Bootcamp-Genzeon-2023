import sqlite3

'Bootcamp2023.db'
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)

details = conn.execute("pragma table_info(participants)")
print(details)

for i in details:
    print(i)
