import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = sl_conn.cursor()

def dbt_create():
    table = '''CREATE TABLE demo_table(
    s text NOT NULL,
    x int NOT NULL,
    y int NOT NULL
    )'''
    curs.execute(table)

dbt_create()

def dbt_insert():
    table2= '''INSERT INTO demo_table VALUES
        ('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7)'''
    curs.execute(table2)
    
dbt_insert()

def dbt_save():
    conn.commit()
    
dbt_save()

# COunting all the rows
def row_count():
    q1= ''' SELECT COUNT (s) FROM demo_table'''
    curs.execute(q1)
    return curs.fetchall()

row_count()

# Query rows greater than 5
def min_count():
    q2 = ''' SELECT COUNT(*) FROM demo_table 
    WHERE x >=5 and y >=5'''
    curs.execute(q1)
    return curs.fetchall()

min_count()

# Counting the Unique y values

def unique_count():
    q4 = '''SELECT COUNT(DISTINCT y) FROM demo_table'''
    curs.execute(q4)
    return curs.fetchall()

unique_count()

