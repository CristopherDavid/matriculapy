class Matricula:

    def __init__(self, placa):
        self.placa = placa.strip()
        self.obtener_digito()
    
    def obtener_digito(self):
        try:
            self.digito = int(self.placa[-1])
        except TypeError:
            raise TypeError("La placa no tiene un formato adecuado")

        