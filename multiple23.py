#programa para verificar que tipo de empleado es segun monto
import os
#declarar variables
remuner1,remuner2=0,0
#Input vias os
remuner1=int(os.sys.argv[1])
remuner2=int(os.sys.argv[2])

#processing
remuneracion_bimestral=remuner1+remuner2
if(remuneracion_bimestral>=900):
    print("empleado publico")
if(remuneracion_bimestral>=1500):
    print("empleado privado")
if(remuneracion_bimestral==200):
    print("empleado estatal")
