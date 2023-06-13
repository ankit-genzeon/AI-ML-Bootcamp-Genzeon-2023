# steps
"""
1. importing sqlite3
2.Create a database
3.establish connection with DB
4.create a table in db_ write query
5.execute query
"""

import sqlite3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)

query = '''
create table participants(g_id int primary key, name text not null, branch text not null, study text not null DEFAULT 'BTech')'''

conn.execute(query)