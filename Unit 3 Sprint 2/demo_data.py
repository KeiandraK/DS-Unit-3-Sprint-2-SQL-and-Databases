import sqlite3
import psycopg2

dbname = 'ywpeznmd'
user = 'ywpeznmd'
password = 'H0syXj4cKi7m-30bHGZmcB-TCHkPIMhr'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM demo_table;')
pg_curs.fetchall()

import sqlite3
sl_conn = sqlite3.connect('demo_data.sqlite3')
sl_curs = sl_conn.cursor()

pg_curs.execute('INSERT INTO demo_table VALUES ("'g'",3,9))