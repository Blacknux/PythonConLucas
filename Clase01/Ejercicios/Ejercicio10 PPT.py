# -*- coding: utf-8 -*-
# Escribir un piedra, papel o tijera de 1 ronda.

import random

opcionesValidas=[1,2,3]

SeleccionMaquina=random.randrange(1,4)
SeleccionHumano=int(input("Seleccione:\n1-Piedra\n2-Papel\n3-Tijera\n"))
print("MAquina",SeleccionMaquina)
if(SeleccionHumano in [1,2,3]):

    if(SeleccionMaquina==SeleccionHumano):
        print("EMPATE")
    elif(SeleccionMaquina==1 and SeleccionHumano==2):
        print("Usted GANO")
        print("Maquina = Piedra Usted=Papel")
    elif(SeleccionMaquina==2 and SeleccionHumano==3):
        print("Usted GANO")
        print("Maquina = Papel Usted=Tijera")
    elif(SeleccionMaquina==3 and SeleccionHumano==1):
        print("Usted GANO")
        print("Maquina = Tijera Usted=Piedra")
    elif(SeleccionMaquina==2 and SeleccionHumano==1):
        print("Usted PERDIO")
        print("Maquina = Papel Usted=Piedra")
    elif(SeleccionMaquina==3 and SeleccionHumano==2):
        print("Usted PERDIO")
        print("Maquina = Tijera Usted=Papel")
    elif(SeleccionMaquina==1 and SeleccionHumano==3):
        print("Usted PERDIO")
        print("Maquina = Piedra Usted=Tijera")
