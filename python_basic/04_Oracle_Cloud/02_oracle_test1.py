import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"/Users/seonggyunjung/instantclient_19_8")

connection = cx_Oracle.connect(user ='PRODUCT', password='Vmfhejrxm123', dsn='db202204141114_high')

cursor = connection.cursor()

cursor.execute('create table pytab(id number, data varchar2(20))')

connection.commit()

