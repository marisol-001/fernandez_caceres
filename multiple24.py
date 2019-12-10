# alumnos en un aula
import os

#declaracion

grado:""
seccion=""
numero_alumnos=0

#Input
grado=str(os.sys.argv[1])
seccion=str(os.sys.argv[2])
numero_alumnos=int(os.sys.argv[3])

#procesing
total=(numero_alumnos)
if(total>30):
    print("excesos_alumnos")
if(total<30):
    print("cantidad_normal_alumnos")
if(total==30):
    print("cantidad_alumnos_establecido")
#fin_if
