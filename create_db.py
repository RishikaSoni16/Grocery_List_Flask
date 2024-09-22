import sqlite3 as sql

#connect to SQLite
con = sql.connect('db_web.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS items")

#Create users table  in db_web database
sql ='''CREATE TABLE "items" (
	"ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"INAME"	TEXT,
	"QUANTITY"	TEXT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()