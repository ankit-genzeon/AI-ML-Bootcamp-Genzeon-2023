import sqlite3

'Bootcamp2023.db'
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)


def fetch_data():
    details = conn.execute("SELECT * FROM participants")
    for i in details:
        print(i)

    conn.commit()
    print("Fetched Succesfully")
    conn.close()