import sqlite3

'Bootcamp2023.db'
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)

query = '''insert into participants values (101, 'Ankit', 'Mech','BTEch','aks282@outlook.com'),
(102 , 'Shubham' , 'Civil' , 'B-Tech' , 'mhaske@gmail.com'),
(103,'Swanand','Mech','Btech','kaleswanand280101@gmail.com'),
(104,'Sudhanshu','ECE','Btech','sudhanshu.rathore@gmail.com')
'''
conn.execute(query)
