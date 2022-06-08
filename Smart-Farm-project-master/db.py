import sqlite3
import os.path 
import datetime

db = "data.db"

def setDatabase():
    file = f"./db/{db}"
    if not os.path.exists(file):
        con = sqlite3.connect("./db/data.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE RaspData(water REAL,groundwater REAL,humidity REAL,temperture REAL, time TEXT);")

def insertData(water, groundwater, humidity, temperture):
    con = sqlite3.connect("./db/data.db")
    cur = con.cursor()
    time = datetime.datetime.now()
    time = str(time).split(".")[0]
    cur.execute("INSERT INTO RaspData (water, groundwater, humidity, temperture, time) VALUES (?,?,?,?,?);", 
    (water, groundwater,humidity, temperture, time))
    con.commit()

def getLastData():
    con = sqlite3.connect("./db/data.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM RaspData ORDER BY ROWID DESC LIMIT 1') #마지막 행 
    con.commit() 
    row = cur.fetchone()
    cur.close()
    return row

# ex
if __name__ == "__main__":
    setDatabase()
    insertData(1,2,3,4)
    print(getLastData())

