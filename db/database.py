import sqlite3
import json

def openConnection():
    conn = sqlite3.connect('db/database.db')
    print("connect success")
    return conn

# conn.row_factory = sqlite3.Row

def addStudent(conn, id, name):
    conn.execute(f"INSERT INTO students (id, name) VALUES ('{id}', '{name}')")
    conn.commit()
    conn.close()

def getStudents(conn, classId):
    cur = conn.cursor()
    cur.execute(f"select * from students where classId='{classId}'")
    rows = cur.fetchall()
    conn.close()
    return rows
    
def getClassTransaction(conn, classId):
    cur = conn.cursor()
    cur.execute(f"select * from class_transaction where classId='{classId}'")
    rows = cur.fetchall()
    conn.close()
    return rows
    
def addClassTransaction(conn, classId, detail, date):
    # try:
    cur = conn.cursor()
    cur.execute(f"INSERT INTO class_transaction (date, classId, detail) VALUES('{date}','{classId}','{json.dumps(detail)}');")
    conn.commit()
    conn.close()
    return True
    # except Exception(e):
    #     return False

def getClasses(conn):
    cur = conn.cursor()
    cur.execute("select * from classes")
    rows = cur.fetchall()
    conn.close()
    return rows

