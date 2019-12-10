import sqlite3
import pandas

df= pd.read_csv(buddymove_holidayiq.csv)

def obtain_name(buddymove_holidayiq.sqlite3, df.to_sql):
    query= 'SELECT * FROM df;'
    
    connection = sqlite3.connect(buddymove_holidayiq.sqlite3)
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return results
    
    