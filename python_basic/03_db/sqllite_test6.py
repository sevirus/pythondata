import sqlite3

def create_table():
    conn = sqlite3.connect('/Users/seonggyunjung/PYTHONDATA/pythondata/python_basic/03_db/books.db')
    cur = conn.cursor()
    cur.execute('''
    create table if not exists books(
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer
    )
    ''')


def insert_book():
    conn = sqlite3.connect('/Users/seonggyunjung/PYTHONDATA/pythondata/python_basic/03_db/books.db')
    cur = conn.cursor()
    title = input('책 이름 >>> ')
    date = input('출판 일자 >>> ')
    publisher = input('출판사 >>> ')
    pages = input('총 페이지 수 >>> ')
    recommend = input('추천 수>>> ')
    data = (title, date, publisher, pages, recommend)
    sql = 'insert into books values(?, ?, ?, ?, ?)'
    cur.execute(sql,data)
    conn.commit()


def list_book():
    conn = sqlite3.connect('/Users/seonggyunjung/PYTHONDATA/pythondata/python_basic/03_db/books.db')
    cur = conn.cursor()
    cur.execute('select * from books')
    data = cur.fetchall()
    for item in data:
        print(f'책 제목 : {item[0]} 출판 일자 : {item[1]} 출판사 : {item[2]} 총 페이지 : {item[3]} 추천 수 : {item[4]}')
    conn.close()


def update_book():
    conn = sqlite3.connect('/Users/seonggyunjung/PYTHONDATA/pythondata/python_basic/03_db/books.db')
    cur = conn.cursor()
    title = input('수정할 책 제목 >>> ')
    col = input('수정할 항목 >>> ')
    value = input('수정할 내용 >>> ')
    sql = f'update books set {col} = ? where title = ?'
    cur.execute(sql,(value,title))
    conn.commit()
    conn.close()


def delete_book():
    conn = sqlite3.connect('/Users/seonggyunjung/PYTHONDATA/pythondata/python_basic/03_db/books.db')
    cur = conn.cursor()
    col = input('삭제할 조건 컬럼 >>> ')
    value = input('삭제할 조건 >>> ')
    sql = f'delete from books where {col} like ?'
    cur.execute(sql, ('%' + value + '%',))
    conn.commit()
    conn.close