from pico_placa import PicoPlaca


#First declaration of PicoPlaca object, just to show the way it works
#Strongly recommended to check the test_picoplaca module
date = "25/02/2021"
plate_number = "PCM-1990"
hour = "19:00"
new_test = PicoPlaca(plate_number,date,hour)
verification = new_test.verify_limitation()
