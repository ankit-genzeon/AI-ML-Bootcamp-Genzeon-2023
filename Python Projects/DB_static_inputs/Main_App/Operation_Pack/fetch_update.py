import sqlite3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)

def update_rec(x,y):
    details = conn.execute("update participants set name = '"+str(y)+"' where g_id = '"+x+"' ")
    conn.commit()
    print("updated")
    conn.close()
