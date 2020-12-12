import sqlite3

#FILE THAT WILL CREATE DATABASE WITH NEEDED TABLES
#RUN ONLY ONCE BEFORE FIRST APP RUN!
conn = sqlite3.connect("data.db")
c = conn.cursor()


c.execute("""CREATE TABLE scatter (id TEXT PRIMARY KEY,x INTEGER ,y INTEGER ,marker TEXT,color TEXT, size REAL)""")
c.execute("CREATE TABLE function (id TEXT PRIMARY KEY ,func TEXT,line TEXT,color TEXT,size REAL)")
c.execute("CREATE TABLE bar (id TEXT PRIMARY KEY ,name TEXT, value INTEGER, color TEXT, width REAL)")
c.execute("CREATE TABLE pie (id TEXT PRIMARY KEY ,slice REAL,activity TEXT,color TEXT,explode REAL)")
c.execute("""   CREATE TABLE noise 
                (id TEXT PRIMARY KEY, 
                seed INTEGER, 
                dispersion_x_positive INTEGER, 
                dispersion_y_positive INTEGER, 
                dispersion_x_negative INTEGER, 
                dispersion_y_negative INTEGER,
                quantity INTEGER,
                color TEXT,
                marker TEXT
                )""")


conn.commit()

conn.close()