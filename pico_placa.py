from matricula import Matricula
from fecha import Fecha
import re
class PicoPlaca:

    def __init__(self,placa,fecha,hora):
        self.matricula = Matricula(placa)
        self.fecha = Fecha(fecha)
        self.hora = hora.strip()
        self.verificar_hora()

    def verificar_hora(self):
        self.on_time = False
        exp_comprobar = '^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
        comprobar = re.search(exp_comprobar,self.hora)
        if comprobar:
            exp_validar = '^(([0]?[78]:[0-5][0-9])|([0]?[9]:([0-2][0-9]|[3][0])))|(([1][678]:[0-5][0-9])|([1][9]:([0-2][0-9]|[3][0])))$'
            valid = re.search(exp_validar,self.hora)
            if valid:
                self.on_time = True
        else:
            raise ValueError("La hora ingresada no es una hora valida")
        
    def verificar_pico(self):
        respuesta = "CIRCULA"
        if self.on_time:
            digito = self.matricula.digito
            dia = self.fecha.dia
            if(((digito == 1 or digito == 2) and dia == 1) or ((digito == 3 or digito == 4) and dia == 2) 
                or ((digito == 5 or digito == 6) and dia == 3) or ((digito == 7 or digito == 8) and dia == 4)
                or ((digito == 9 or digito == 0) and dia == 5)):
                respuesta = "NO CIRCULA" 
        return respuesta