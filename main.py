print('Welcome to our Restaurant')
print('Book your table here')
import sqlite3



# Connecting the database
def db_conn():
    connex = None
    try:
        connex = sqlite3.connect('ReservationInfo.sqlite')
    except sqlite3.error as e:
        print(e)
    return connex

class Info:
#This class is used for getting the information of customer.
    def __init__(self, fname:str, lname:str, date: int, time: int, phone:int, num_persons: int):
        self.fname = fname
        self.lname = lname
        self.date = date
        self.time = time
        self.phone = phone
        self.num_persons = num_persons
        

    def print_info(self, lname):
        if self.lname == lname:
            print(f'Yes, the name {self.lname} has a reservation on {self.date} at {self.time} for {self.num_persons} person(s).')

        else:
            print('No information available for this name.')



class InsertReservation:
#   Creating a class method that will allow users to add new reservations 
    def __init__(self):
        self.fname = input('Name: ')
        self.lname = input('Last Name: ')
        self.date = (input('Date (DD/MM/YYYY): '))
        self.time = (input("Time (HH:mm) "))
        self.phone = int(input("Phone number: "))
        self.num_persons = int(input('Number of persons: '))
        
        print('Attend for availability...')

    # Function to insert data into database
    def insert_personal_data(self):
        self.connex = db_conn()
        self.cur = self.connex.cursor()
        sql = """INSERT INTO Info (fname, lname, date, time, phone, num_person) VALUES(?,?,?,?,?,?)"""
        self.cur = self.cur.execute(sql,(self.fname,self.lname,self.date,self.time,self.phone,self.num_persons))
        self.connex.commit()
        self.connex.close()
        return ("Your Reservation has been registered!")


    #Checking for availability
    # def check_availability(self):
    #     connex = db_conn()
    #     cur = connex.cursor()
    #     cur.execute("SELECT lname FROM Info")
    #     result = cur.fetchone()

        
        
reservation =  InsertReservation()
my_table = Info(reservation.fname,reservation.lname,reservation.date,reservation.time,reservation.phone,reservation.num_persons)
my_table.print_info('boutsis') 
#reservation.insert_personal_data()