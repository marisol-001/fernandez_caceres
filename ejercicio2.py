#ejercicio2
import  os
#declaracion de variables
compra1,compra2,compra3,monto_total=0,0,0,0

compra1=int(os.sys.argv[1])
compra2=int(os.sys.argv[2])
compra3=int(os.sys.argv[3])

monto_total=compra1+compra2+compra3

#processing
if(monto_total>200):
    print(monto_total,"saldo insuficiente")
