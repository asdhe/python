from cmath import log
import sqlite3
import sys

db_dir = sys.path[0] + '/login.db'


class db():
    def __init__(self) -> None:
        pass

    def createDB(self):
        con = sqlite3.connect(db_dir)
        cur = con.cursor()
        sql = ''' 
        CREATE TABLE Student(
        ID     INT    PRIMARY KEY,
        NAME   TEXT  NOT NULL,
        CLASS   INT   NOT NULL,
        ACADEMY TEXT   NOT NULL);
        '''
        try:
            cur.execute(sql)
        except BaseException as e:
            print(e)
        finally:
            cur.close()
            con.close()

    def insertDB(self):
        con = sqlite3.connect(db_dir)
        cur = con.cursor()
        insert_many_sql = """INSERT into Student(ID,NAME,CLASS,ACADEMY) values(?,?,?,?);"""
        data_list = [(202121147072, 'HJH', 2103, "College of Computer Science and Technology"),
                     (202121147073, 'ZS', 2103, "College of Computer Science and Technology"),
                     (202121147074, 'LS', 2103, "College of Computer Science and Technology"),
                     (202121147075, 'WW', 2103, "College of Computer Science and Technology")]
        try:
            cur.executemany(insert_many_sql, data_list)
            con.commit()
        except BaseException as e:
            print(e)
            con.rollback()
        finally:
            cur.close()
            con.close()

    def checkDB(self):
        con = sqlite3.connect(db_dir)
        cur = con.cursor()
        sql = "select * from Student"
        try:
            values = cur.execute(sql)
            for p in values:
                print(p)
            con.commit()
        except BaseException as e:
            print(e)
            print("commit failed")
            con.rollback()
        finally:
            cur.close()
            con.close()


a = db()
a.createDB()
a.insertDB()
a.checkDB()
