import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

con = sqlite3.connect('/Users/seonggyunjung/PYTHONDATA/pythondata/python_basic/03_db/example.db')

cur = con.cursor()

cur.execute('''CREATE TABLE stock(
                data text, 
                trans text, 
                symbol text, 
                qty real, 
                price real
)'''

)
cur.execute("INSERT INTO stock VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

con.commit()

con.close()