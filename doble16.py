#ejercicio20 doble
import os
#declarar variables
preciodecompra,preciodeventa,monto=0,0,0
preciodecompra=int(os.sys.argv[1])
preciodeventa=int(os.sys.argv[2])
monto=preciodecompra+preciodeventa

#procesing
if(monto>500):
    print("monto alto")
else:
    print("monto bajo")
#fin-if
