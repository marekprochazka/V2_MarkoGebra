import sqlite3

conn = sqlite3.connect("data.db")
c = conn.cursor()


c.execute("""CREATE TABLE scatter (id integer primary key AUTOINCREMENT,x INTEGER ,y INTEGER ,marker TEXT,color TEXT, size REAL)""")
c.execute("CREATE TABLE function (id integer primary key AUTOINCREMENT,func TEXT,line TEXT,color TEXT,size REAL)")
c.execute("CREATE TABLE bar (id integer primary key AUTOINCREMENT,name TEXT, value TEXT, color TEXT)")
c.execute("CREATE TABLE pie (id integer primary key AUTOINCREMENT,slice REAL,activity TEXT,color TEXT,explode REAL)")
#TODO finish random noise


conn.commit()

conn.close()