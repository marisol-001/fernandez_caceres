#ejercicio 22 doble
import os
#Declarar
Usuario=""
clave=""
#Input via os
Usuario=str(os.sys.argv[1])
clave=str(os.sys.argv[2])
#processing
if (Usuario=="sol")and(clave=="1234"):
  print("Acceso correcto")
else:
    print("Acceso incorrecto")
#fin_if
