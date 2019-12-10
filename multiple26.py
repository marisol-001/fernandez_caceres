#curso reprobado
import os
#declarar
alumno=""
nota1=0
nota2=0
nota3=0

#input
alumno=str(os.sys.argv[1])
nota1=int(os.sys.argv[2])
nota2=int(os.sys.argv[3])
nota3=int(os.sys.argv[4])

#Procesing
promedio=(nota1+ nota2 + nota3) /3
if (promedio<10.5):
    print("reprobo el curso")
if(promedio>10.5)and(promedio<=16):
    print("regular")
if(promedio>=17)and(promedio<=20):
    print("excelente")
#fin_if
