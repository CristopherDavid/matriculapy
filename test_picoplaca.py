import unittest
from pico_placa import PicoPlaca

class testPico(unittest.TestCase):

    def test_verificacion(self):
        fecha = "24/02/2021"
        placa = "PCM-1996"
        hora = "9:31"
        verif = PicoPlaca(placa,fecha,hora)
        self.assertEqual(verif.verificar_pico(),'CIRCULA')
        fecha = "26/02/2021"
        placa = "PCM-1990     "
        hora = "7:31"
        verif = PicoPlaca(placa,fecha,hora)
        self.assertEqual(verif.verificar_pico(),'NO CIRCULA')
        fecha = "   26-02-2021   "
        placa = "PCM-1990     "
        hora = "6:59    "
        verif = PicoPlaca(placa,fecha,hora)
        self.assertEqual(verif.verificar_pico(),'CIRCULA')
        fecha = "   25-02-2021   "
        placa = " PCM-1998     "
        hora = "15:59    "
        verif = PicoPlaca(placa,fecha,hora)
        self.assertEqual(verif.verificar_pico(),'CIRCULA')
        fecha = "   5/3/2021   "
        placa = " PCM-1990     "
        hora = "19:29    "
        verif = PicoPlaca(placa,fecha,hora)
        self.assertEqual(verif.verificar_pico(),'NO CIRCULA')



if __name__ == '__main__':
    unittest.main()