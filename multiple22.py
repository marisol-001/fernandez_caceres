#calcular monto total de productos de aseo
import os

#declarar variables
prod1,prod2,prod3=0,0,0

#Input via os
prod1=int(os.sys.argv[1])
prod2=int(os.sys.argv[2])
prod3=int(os.sys.argv[3])

#processing
monto_productos=prod1+prod2+prod3

if(monto_productos==400):
    print("ganaste una colonia")

if(monto_productos==600):
    print("ganaste 3 colonias")
if(monto_productos==1000):
    print("ganaste un viaje")
