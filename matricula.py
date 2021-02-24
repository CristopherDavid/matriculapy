class Plate():

    def __init__(self, plate_number):
        self.plate_number = plate_number.strip()
        self.get_last_digit()
    
    def get_last_digit(self):
        try:
            self.last_digit = int(self.plate_number[-1])
        except TypeError:
            raise TypeError("The plate number format is incorrect")

        