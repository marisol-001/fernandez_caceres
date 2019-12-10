#programa para calcular los montos totales de compras
import os
comp1,comp2,comp3,comp4=0,0,0,0
#Input via os
comp1=int(os.sys.argv[1])
comp2=int(os.sys.argv[2])
comp3=int(os.sys.argv[3])
comp4=int(os.sys.argv[4])

#Processing
monto_total=comp1+comp2+comp3+comp4

#condicion multiple
if(monto_total>=30)and(monto_total<=60):
    print("monto bajo")
if(monto_total>=100)and(monto_total<=150):
    print("monto regular")
if(monto_total>=200)and(monto_total<=400):
    print("monto elevado")
