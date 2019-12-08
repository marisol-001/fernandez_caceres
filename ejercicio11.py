#ejercicio 11
import os

#declaracion de variables

trabajador=""
remumeracion_mensual=0.0
numero_de_meses=0
remuneracion=0

#Input via os
trabajador=str(os.sys.argv[1])
remumeracion_mensual=float(os.sys.argv[2])
numero_de_meses=int(os.sys.argv[3])

#PROCESSING
remuneracion=remumeracion_mensual*numero_de_meses
if (remuneracion>4000):
    print("tiene remuneracion anual")
#fin_if
