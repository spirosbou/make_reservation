print('Welcome to our Restaurant')
print('Book your table here')

class Info:

    def __init__(self, name:str, date: int, phone:int, num_persons: int):
        self.name = name
        self.date = date
        self.phone = phone
        self.num_persons = num_persons
        #self.res_id = res_id

    def print_info(self, name):
        if self.name == name:
            print(f'Yes, the name, {self.name} has a reservation on  {self.date} for {self.num_persons} person(s).')

        else:
            print('No information available for this name.')



class InsertReservation:

    def __init__(self):
        self.name = input('Name: ')
        self.date = (input('Date (DD/MM/YYYY): '))
        self.time = (input("Time (HH:mm) "))
        self.phone = int(input("Phone number: "))
        self.num_persons = int(input('Number of persons: '))
    
        print('Attend for availability...')
        
        
reservation =  InsertReservation()
my_table = Info(reservation.name, reservation.date, reservation.phone, reservation.num_persons)
my_table.print_info('spiros') 