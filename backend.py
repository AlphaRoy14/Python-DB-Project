import sqlite3

def connect():
    conn=sqlite3.connect("books.db") #connecting to the database
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books ( id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()


    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books  WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))  #the coma next to id is nescessary
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE books SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))  #the coma next to id is nescessary
    conn.commit()
    conn.close()



connect()
# insert("Sex","ramu",2018,1)
# insert("django","ning",2019,2)
