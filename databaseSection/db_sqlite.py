import sqlite3

# If don't have lite.db,it is going to create by own.
#5 steps for db:
# connection
# openning a cursor for sql data
# executing SQL
# commiting transaction
# closing connection
def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item text,quantity integer,price real)")
    cur.execute("INSERT INTO STORE VALUES('WINE GLASS',8,100)")
    conn.commit()
    conn.close()

def insert_data(items, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO STORE VALUES(?,?,?)",(items,quantity,price))
    conn.commit()
    conn.close()

def view_data():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("select * from store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_data(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("delete from store where item=?",(item,))
    conn.commit()
    conn.close()

def update_data(price,item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("update store set price=? where item=?",(price,item,))
    conn.commit()
    conn.close()


# insert_data("Coffee Cup",2,10)
# delete_data("WINE GLASS")
update_data(20,"Tea Cup")
print(view_data())