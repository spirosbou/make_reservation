print('Welcome to our Restaurant')
print('Book your table here')

class Info:

    def __init__(self, name:str, date: int, phone:int, num_persons: int):
        self.name = name
        self.date = date
        self.phone = phone
        self.num_persons = num_persons

class Action:

    def reservation(self, object_par):
        self.object_par = object_par

        reserv = {}
        
