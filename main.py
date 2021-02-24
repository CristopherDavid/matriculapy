from pico_placa import PicoPlaca

fecha = "   26/02/2021   "
placa = " PCM-1990     "
hora = "16:42    "
nueva_comprobacion = PicoPlaca(placa=placa,fecha=fecha,hora=hora)
verificacion = nueva_comprobacion.verificar_pico()
