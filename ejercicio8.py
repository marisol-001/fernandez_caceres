#ejercicio 8
import os
#declarar
lado1,lado2,area=0.0,0.0,0.0
#Input via os
lado1=float(os.sys.argv[1])
lado2=float(os.sys.argv[2])

area=lado1*lado2

#processing
if(area>60):
    print("cuadrado grande")

#fin_if
