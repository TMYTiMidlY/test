import sqlite3

conn = sqlite3.connect("text.db")
c = conn.cursor()
sql1 = '''
    insert into company(id,name,age,salary)
    values(1,"哈哈",32,8000);
'''
c.execute('''CREATE TABLE company
    (id int primary key not null,
         name text not null,
        age int not null,
        salary real);
''')
c.execute(sql1)
conn.commit()
conn.close()