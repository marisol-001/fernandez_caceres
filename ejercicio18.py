#ejercicio 18

import os
#declarar
tiempodesalida,tiempodellegada,tiempo_total=0,0,0

tiempodesalida=int(os.sys.argv[1])
tiempodellegada=int(os.sys.argv[2])
tiempo_total=tiempodesalida+tiempodellegada

#procesing
if(tiempo_total>50):
    print(tiempo_total,"velocidad excelente")
else:
    print(tiempo_total,"velocidad pesima")
#fin-if
