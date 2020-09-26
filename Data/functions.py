import sqlite3
from Static.constants import DELETE,CREATE,UPDATE

conn = sqlite3.connect("data.db")
c = conn.cursor()

def get_table(name):
    c.execute("SELECT * FROM ?",name)
    return c.fetchall()

def update_scatter(changes):
    for change in changes:
        if change["action"] == CREATE:
            c.execute("""   INSERT INTO scatter(x,y,marker,size,color) 
                            VALUES (?,?,?,?,?)"""
                      ,change["data"])

        elif change["action"] == UPDATE:
            c.execute("""   UPDATE scatter 
                            SET x=?,y=?,marker=?,size=?,color=?
                            WHERE id=?"""
                      ,change["data"] + change["id"])
        elif change["action"] == DELETE:
            c.execute("DELETE FROM scatter WHERE id=?",change["id"])
    conn.commit()

def update_func(values):
    c.executemany("INSERT INTO function(func,line,color,size) VALUES (?,?,?,?)",values)
    conn.commit()

def update_pie(values):
    c.executemany("INSERT INTO pie(slice,activity,color,explode) VALUES (?,?,?,?)",values)
    conn.commit()

def update_bar(values):
    c.executemany("INSERT INTO bar(name,value,color) VALUES (?,?,?)",values)
    conn.commit()


changes = [{"action":UPDATE,"data":(3,3,":-)",6,"aqua"),"id":(1,)},{"action":DELETE,"id":(2,)},{"action":CREATE,"data":(1,2,"*",3,"blue")},{"action":CREATE,"data":(1,2,"*",3,"blue")}]
update_scatter(changes)