from matricula import Plate
from fecha import DateObject
import re

DATE_DICTIONARY = {
    '1':[1,2],
    '2':[3,4],
    '3':[5,6],
    '4':[7,8],
    '5':[9,0],
}
class PicoPlaca:
    
    def __init__(self,plate_number,date,hour):
        self.plate = Plate(plate_number)
        self.date = DateObject(date)
        self.hour = hour.strip()
        self.hour_verification()

    def hour_verification(self):
        
        self.is_range = False
        #Verification by regex if the string we get is a valid 24h hour
        hour_validation_regex = '^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
        is_valid = re.search(hour_validation_regex,self.hour)
        if is_valid:
            #Verification by regex if the hour we get is in the range of no circulation 7:00 - 9:30 and 16:00 - 19:00
            hour_range_regex = '^(([0]?[78]:[0-5][0-9])|([0]?[9]:([0-2][0-9]|[3][0])))|(([1][678]:[0-5][0-9])|([1][9]:([0-2][0-9]|[3][0])))$'
            is_in_range = re.search(hour_range_regex,self.hour)
            if is_in_range:
                self.is_range = True
        else:
            raise ValueError("The hour entered it's not a valid hour")
        
    def verify_limitation(self):
        response = "CIRCULA"
        if self.is_range:
            digit = self.plate.last_digit
            day = self.date.day
            #Verification if the list of the index under the day key has one of the digit restricted that day
            if digit in DATE_DICTIONARY[day]:
                response = "NO CIRCULA"
        return response