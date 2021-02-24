from datetime import datetime

class Fecha():

    def __init__(self,cadena):
        self.cadena = cadena.strip()
        self.validar_fecha()
        self.obtener_dia()

    def validar_fecha(self):
        if(self.cadena.find('/') != -1):
            template = '%d/%m/%Y'
        elif(self.cadena.find('-') != -1):
            template = '%d-%m-%Y'
        else:
            template = None
        try:
            self.date = datetime.strptime(self.cadena,template)
        except ValueError:
            raise ValueError("La fecha ingresada no es adecuada")
        except TypeError:
            raise TypeError("El formato de fecha es incorrecto")
        

    def obtener_dia(self):
        self.dia = int(self.date.strftime('%w'))
              