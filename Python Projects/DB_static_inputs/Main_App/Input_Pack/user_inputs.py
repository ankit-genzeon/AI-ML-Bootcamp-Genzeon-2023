import sqlite3

'Bootcamp2023.db'
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)

def input_data():
    data = {}
    g_id = int(input("Enter G_id: "))
    name = input("Enter Name: ")
    branch = input("Enter branch: ")
    study = input("Enter Study: ")
    data["g_id"] = g_id
    data["name"] = name
    data["branch"] = branch
    data["study"] = study

    conn.execute('''
    insert into participants (G_id,name,branch,study) values(?,?,?,?)
    ''', (data["g_id"], data["name"], data["branch"], data["study"]))
    conn.commit()
