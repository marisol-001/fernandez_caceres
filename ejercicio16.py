#ejercicio 16 dobles
import os
#declarar variables
nombre,edad="",0

nombre=os.sys.argv[1]
edad=int(os.sys.argv[2])

#processing
if(edad>35):
    print(nombre,"adulto")
else:
    print(nombre,"joven")


#fin_if
