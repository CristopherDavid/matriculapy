import unittest
from pico_placa import PicoPlaca

class TestPico(unittest.TestCase):

    def test_verificacion(self):
        date = "24/02/2021"
        plate_number = "PCM-1996"
        hour = "9:31"
        verification = PicoPlaca(plate_number,date,hour)
        self.assertEqual(verification.verify_limitation(),'CIRCULA')
        date = "26/02/2021"
        plate_number = "PCM-1990     "
        hour = "7:31"
        verification = PicoPlaca(plate_number,date,hour)
        self.assertEqual(verification.verify_limitation(),'NO CIRCULA')
        date = "   26-02-2021   "
        plate_number = "PCM-1990     "
        hour = "6:59    "
        verification = PicoPlaca(plate_number,date,hour)
        self.assertEqual(verification.verify_limitation(),'CIRCULA')
        date = "   25-02-2021   "
        plate_number = " PCM-1998     "
        hour = "15:59    "
        verification = PicoPlaca(plate_number,date,hour)
        self.assertEqual(verification.verify_limitation(),'CIRCULA')
        date = "   5/3/2021   "
        plate_number = " PCM-1990     "
        hour = "19:29    "
        verification = PicoPlaca(plate_number,date,hour)
        self.assertEqual(verification.verify_limitation(),'NO CIRCULA')



if __name__ == '__main__':
    unittest.main()