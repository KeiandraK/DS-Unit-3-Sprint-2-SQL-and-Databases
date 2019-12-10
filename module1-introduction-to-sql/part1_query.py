import sqlite3

class SQL:
    def __init__(self, sql):
        "execute?"
        self.dbpath = sql
        self.conn = sqlite3.connect(sql)
        
    def query(self, query):
        "SQL info here"
        curs = self.conn.cursor()
        result - curs.execute(query).fetchall()
        curs.close()
        self.conn.commit
        return result