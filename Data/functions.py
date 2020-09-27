import sqlite3
from Static.constants import DELETE,CREATE,UPDATE,ACTION,DATA,ID,TYPE,FUNCTION,SCATTER, MATH, PIE, BAR
from Data.path import get_path

from Utils.uuid import generate_uuid, format_existing_uuid


conn = sqlite3.connect(get_path()+"\data.db")
c = conn.cursor()

def get_table(name):
    c.execute("SELECT * FROM {}".format(name))
    return c.fetchall()

def delete_all_from_table(name):
    c.execute("DELETE FROM {};".format(name))
    conn.commit()

def update_math(changes):
    for change in changes:
        if change[TYPE] == SCATTER:
            if change[ACTION] == CREATE:
                c.execute("""   INSERT INTO scatter 
                                VALUES (?,?,?,?,?,?)"""
                          ,change[ID] + change[DATA])

            elif change[ACTION] == UPDATE:
                c.execute("""   UPDATE scatter 
                                SET x=?,y=?,marker=?,size=?,color=?
                                WHERE id=?"""
                          ,change[DATA] + change[ID])
            elif change[ACTION] == DELETE:
                c.execute("DELETE FROM scatter WHERE id=?",change[ID])
        elif change[TYPE] == FUNCTION:
            if change[ACTION] == CREATE:
                c.execute("""   INSERT INTO function
                                VALUES (?,?,?,?,?)"""
                          , change[ID] + change[DATA])
            elif change[ACTION] == UPDATE:
                c.execute("""   UPDATE function
                                SET func=?,line=?,color=?,size=?
                                WHERE id=?"""
                          , change[DATA] + change[ID])
            elif change[ACTION] == DELETE:
                c.execute("DELETE FROM function WHERE id=?", change[ID])

    conn.commit()



def update_pie(changes):
    for change in changes:
        if change[ACTION] == CREATE:
            c.execute("""   INSERT INTO pie
                            VALUES (?,?,?,?,?)"""
                      ,change[ID] + change[DATA])
        elif change[ACTION] == UPDATE:
            c.execute("""   UPDATE pie
                            SET slice=?,activity=?,color=?,explode=?
                            WHERE id=?"""
                      ,change[DATA] + change[ID])
        elif change[ACTION] == DELETE:
            c.execute("DELETE FROM pie WHERE id=?",change[ID])
    conn.commit()

def update_bar(changes):
    for change in changes:
        if change[ACTION] == CREATE:
            c.execute("""   INSERT INTO bar
                            VALUES (?,?,?,?)"""
                      ,change[ID] + change[DATA])
        elif change[ACTION] == UPDATE:
            c.execute("""   UPDATE bar
                            SET name=?,value=?,color=?
                            WHERE id=?"""
                      ,change[DATA] + change[ID])
        elif change[ACTION] == DELETE:
            c.execute("DELETE FROM bar WHERE id=?",change[ID])
    conn.commit()


UPDATE_FUNCTIONS = {MATH:update_math,BAR:update_bar,PIE:update_pie}

# changes = [{ACTION: CREATE,DATA:(3,3,"aa",7,"pink"),ID:(str(uuid.uuid4()),),TYPE:SCATTER},{ACTION:CREATE,DATA:("y**2","- -","red",8),ID:(str(uuid.uuid4()),),TYPE:FUNCTION}]
# update_math(changes)

# changes = [{ACTION:UPDATE,DATA:(8,"asdfasdf","rred",17),ID:format_existing_uuid("a67cbec5-5e7e-4563-b310-0a23467b2057")},
#            {ACTION:CREATE,DATA:(7,"jksdhfg","pnk",11),ID:generate_uuid()},
#            {ACTION:DELETE,ID:format_existing_uuid("c5f8ec82-006b-46f5-9335-f94d1de7b7aa")}]
# update_pie(changes)

# changes = []
# import random
# for _ in range(2000):
#     changes.append({ACTION:CREATE,DATA:(str(random.randrange(0,500)),random.randrange(0,500),"red"),ID:generate_uuid()})
#
# update_bar(changes)

# delete_all_from_table("bar")