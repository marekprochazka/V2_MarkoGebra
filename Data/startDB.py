import sqlite3

conn = sqlite3.connect("data.db")
c = conn.cursor()


c.execute("""CREATE TABLE scatter (id TEXT PRIMARY KEY ,x INTEGER ,y INTEGER ,marker TEXT,color TEXT, size REAL)""")
c.execute("CREATE TABLE function (id TEXT PRIMARY KEY ,func TEXT,line TEXT,color TEXT,size REAL)")
c.execute("CREATE TABLE bar (id TEXT PRIMARY KEY ,name TEXT, value INTEGER, color TEXT, width REAL)")
c.execute("CREATE TABLE pie (id TEXT PRIMARY KEY ,slice REAL,activity TEXT,color TEXT,explode REAL)")
#TODO finish random noise


conn.commit()

conn.close()