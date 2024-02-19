import sqlite3


def db_conn():
    connex = None
    try:
        connex = sqlite3.connect('Reservation_db')
    except sqlite3.error as e:
        print(e)
    return connex

def get_customer_info():
    connex = db_conn()
    cursor = connex.cursor()

    cursor.execute("SELECT * FROM Info WHERE LAST_NAME=?", (input('Enter last name: '),)) 
    
    data = cursor.fetchone()
    if data is None:
        print("No customer with that last name.")
    else:
        print('Yes the customer has a reservation.')


get_customer_info()