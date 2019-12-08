#ejercicio 15
import os

#declaracion de variables
institucion=""
grado:""
seccion=""
numero_alumnos=0

#Input via os
institucion=str(os.sys.argv[1])
grado=str(os.sys.argv[2])
seccion=str(os.sys.argv[3])
numero_alumnos=int(os.sys.argv[4])

#procesing
total=(numero_alumnos)
if(total>30):
    print("exceso_alumnos_en_aula")
#fin_if
