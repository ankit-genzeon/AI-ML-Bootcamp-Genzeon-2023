import sqlite3

'Bootcamp2023.db'
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)


def fetch_branch(inp_branch):
    x=input("Enter Branch : ")
    details = conn.execute("select * from participants where branch ='"+str(x)+"' ")
    for i in details:
        print(i)

    conn.commit()
    print("Fetched")
    conn.close()