from datetime import datetime

class DateObject():

    def __init__(self,string_date):
        self.string_date =string_date.strip()
        self.date_validation()
        self.get_day_number()

    def date_validation(self):
        #Date format validation we can have '-' or '/' as our date separator
        if(self.string_date.find('/') != -1):
            template = '%d/%m/%Y'
        elif(self.string_date.find('-') != -1):
            template = '%d-%m-%Y'
        else:
            template = None
        try:
            self.date = datetime.strptime(self.string_date,template)
        except ValueError:
            raise ValueError("The date you entered is incorrect")
        except TypeError:
            raise TypeError("El date format is incorrect")
        

    def get_day_number(self):
        self.day = self.date.strftime('%w')
              