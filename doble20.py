# ejercicio 24
import os
#declaracion
nombre=""
acciones=0
total=0

#Input via os
nombre=str(os.sys.argv[1])
acciones=int(os.sys.argv[2])


#procesing
total=acciones
if(total>10):
    print(nombre,"socio_mayoritario")
else:
    print(nombre,"socio_minoritario")
#fin_if
