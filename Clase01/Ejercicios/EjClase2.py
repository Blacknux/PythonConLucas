# -*- coding: utf-8 -*-
import time
import os
import webbrowser
import winsound

url=input("Ingrese la Url que desea que se abra: ")
timeToBreak=int(input("Ingrese cada cuantos minutos desea tomarse un break: "))#*60
breakTime=int(input("Cuanto dura su break? "))#*60
continuee="s"

#print(timeToBreak)
time.sleep(timeToBreak)
while(continuee !="N" ):
    time.sleep(timeToBreak)
    webbrowser.open(url)
    time.sleep(breakTime)
    print("Hora de trabajar!!!! ")
    for x in range(20):
        winsound.Beep(6000 , 500)
    continuee=input("Continuamos con el programa Brekero? S=si / N=no ")
    continuee=continuee.upper()

print( "Buen Descanso \n Presione una tecla para cerrar la ventana....")
input()


