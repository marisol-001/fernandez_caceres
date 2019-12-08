#EJERCICIO 01
import os
#declaracion
nota1=0.0
nota2=0.0
nota3=0.0
nota4=0.0

#Input

nota1=float(os.sys.argv[1])
nota2=float(os.sys.argv[2])
nota3=float(os.sys.argv[3])
nota4=float(os.sys.argv[4])

#procesing
promedio=(nota1+nota2+nota3+nota4)/4
if(promedio>10.5):
    print("curso aprobado")
#fin_if
