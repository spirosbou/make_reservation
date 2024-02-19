import sqlite3

connex = sqlite3.connect('ReservationInfo')

cursor = connex.cursor()

sql_query = """CREATE TABLE IF NOT EXISTS Info(
            ID INTEGER PRIMARY KEY,
            fname TEXT NOT NULL, 
            lname TEXT NOT NULL,
            date TEXT NOT NULL,
            time  TEXT NOT NULL,
            phone INTEGER NOT NULL,
            num_persons INTEGER NOT NULL
)"""

cursor.execute(sql_query)