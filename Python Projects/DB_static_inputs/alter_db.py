import sqlite3

'Bootcamp2023.db'
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)

'''
add column - mail_id
Alter table table_name add column column_name datatype constraints'''

# conn.execute('''
# alter table participants add column mail_id text not null''')

conn.execute('''update participants set name = 'Mhaske' where name = 'shubham'
''')
