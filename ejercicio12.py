#ejercicio 12
import os

#Declarar variables
precio=0.0
igv=0.0
total_pago_igv=0

#Input vias os
precio=float(os.sys.argv[1])
igv=float(os.sys.argv[2])

#PROCESING
total_pago_igv=precio*igv
if (total_pago_igv>50):
    print("igv")
#fin_if
