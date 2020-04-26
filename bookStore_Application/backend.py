import sqlite3
class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books(id integer primary key,title text,author text,year integer,isbn integer)")
        self.conn.commit()

    def insert_data(self,title,author,year,ISBN):
        self.cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,ISBN))
        self.conn.commit()

    def view_data(self):
        self.cur.execute("select * from books")
        rows = self.cur.fetchall()
        return rows

    def search_data(self,title="",author="",year="",isbn=""):
        self.cur.execute("select * from books where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
        rows = self.cur.fetchall()
        return rows

    def delete_data(self,id):
        self.cur.execute("delete from books where id=?",(id,))
        self.conn.commit()

    def update_data(self,id,title,author,year,ISBN):
        self.cur.execute("update books set title=?,author=?,year=?,isbn=? where id=?",(title,author,year,ISBN,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    # create_table()
    # insert_data("the sea","johny",2008,12345)
    # print(view_data())
    # print(search_data(author="john"))
    # update_data(1,"The earth","harvey",1915,235654)
    # print(view_data())