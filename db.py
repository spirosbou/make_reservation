import sqlite3

connex = sqlite3.connect('ReservationInfo.sqlite')

cursor = connex.cursor()

sql_query = """ CREATE TABLE Reservations (
            id integer PRIMARY KEY,
            name text NOT NULL,
            date text NOT NULL,
            phone integer NOT NULL,
            num_persons integer NOT NULL
)"""

cursor.execute(sql_query)