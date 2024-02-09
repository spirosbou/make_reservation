print('Welcome to our Restaurant')
print('Book your table here')

class Info:

    def __init__(self, fname:str, lname:str, phone:int):
        self.fname = fname
        self.lname = lname
        self.phone = phone

class Action:

    def __init__(self, fname, lname, phone):
        self.info = Info(fname, lname, phone)
        