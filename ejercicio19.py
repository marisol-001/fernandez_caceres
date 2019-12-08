#ejercicio19 doble
import os
#declarar las variables
talla1,talla2,tallafinal=0,0,0

talla1=int(os.sys.argv[1])
talla2=int(os.sys.argv[2])

tallafinal=talla2+talla1
#preocesing
if(tallafinal<60):
    print("tratamiento bueno")
else:
    print("tratamiento malo")

#fin-if
