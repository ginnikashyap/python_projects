import psycopg2

# If don't have dbname='test' user='postgres,it is going to create by own.
#5 steps for db:
# connection
# openning a cursor for sql data
# executing SQL
# commiting transaction
# closing connection
def create_table():
    conn = psycopg2.connect("dbname='test' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item text,quantity integer,price real)")
    cur.execute("INSERT INTO STORE VALUES('WINE GLASS',8,100)")
    conn.commit()
    conn.close()

def insert_data(items, quantity, price):
    conn = psycopg2.connect("dbname='test' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO STORE VALUES(%s,%s,%s)",(items,quantity,price))
    conn.commit()
    conn.close()

def view_data():
    conn = psycopg2.connect("dbname='test' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("select * from store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_data(item):
    conn = psycopg2.connect("dbname='test' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("delete from store where item=%s",(item,))
    conn.commit()
    conn.close()

def update_data(price,item):
    conn = psycopg2.connect("dbname='test' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("update store set price=%s where item=%s",(price,item,))
    conn.commit()
    conn.close()

create_table()

insert_data("Juice Cup",2,10)
# delete_data("WINE GLASS")
update_data(20,"Juice Cup")
print(view_data())