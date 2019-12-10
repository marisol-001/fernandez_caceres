#edad
import os
#declaracion
nombre=""
año_nacimiento=0
año_actual=0

#Input
nombre=str(os.sys.argv[1])
año_nacimiento=int(os.sys.argv[2])
año_actual=int(os.sys.argv[3])

#procesing
edad=(año_actual - año_nacimiento)
if(edad<11):
    print("niño")
if(edad>11)and(edad<=19):
    print("adolescente")
if(edad>19)and(edad<30):
    print("joven")
#fin_if
