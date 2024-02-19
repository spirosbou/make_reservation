import sqlite3



def db_conn():
    
    connex = None
    try:
        connex = sqlite3.connect('Reservation_db')
    except sqlite3.error as e:
        print(e)
    return connex


def  create_table():
    connex = db_conn()
    cur = connex.cursor()
    table = """CREATE TABLE IF NOT EXISTS Info(
            id integer primary key,
            first_name varchar(20) not null,
            last_name varchar(20) not null,
            date text not null,
            time text not null,
            phone_number integer not null,
            num_persons integer not null
    )"""
    cur.execute(table)
    connex.close()


def  insert_data():
    connex = db_conn()
    cur = connex.cursor()
    first_name = input('First name:')
    last_name = input('Last Name : ')
    date = input("Enter the Date (DD-MM-YY):")
    time = input("Enter Time in format HH:MM ")
    phone = int(input("Phone number:"))
    persons = int(input("Number of Persons:"))
    customer_data = """INSERT INTO Info(first_name,last_name,date,time,phone_number,num_persons) VALUES(?,?,?,?,?,?)"""
    cur.execute(customer_data, (first_name,last_name,date,time,phone,persons))
    data = cur.execute('SELECT * FROM Info')

    for  i in data:
        print(i)

    connex.commit()
    connex.close()
    print("Data inserted successfully!")


create_table()
insert_data()


