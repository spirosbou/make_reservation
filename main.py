print('Welcome to our Restaurant')
print('Book your table here')
import time
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
    def __init__(self, name:str, date: int, phone:int, num_persons: int):
        self.name = name
        self.date = date
        self.phone = phone
        self.num_persons = num_persons
        

    def print_info(self, name):
        if self.name == name:
            print(f'Yes, the name {self.name} has a reservation on  {self.date} for {self.num_persons} person(s).')

        else:
            print('No information available for this name.')



class InsertReservation:
#   Creating a class method that will allow users to add new reservations 
    def __init__(self):
        self.name = input('Name: ')
        self.date = (input('Date (DD/MM/YYYY): '))
        self.time = (input("Time (HH:mm) "))
        self.phone = int(input("Phone number: "))
        self.num_persons = int(input('Number of persons: '))
    
        print('Attend for availability...')
        time.sleep(3)

    #Checking for availability
    def check_availability(self):
        pass
        
        
reservation =  InsertReservation()
my_table = Info(reservation.name, reservation.date, reservation.phone, reservation.num_persons)
my_table.print_info('spiros') 