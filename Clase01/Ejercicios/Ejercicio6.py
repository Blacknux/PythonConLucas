# -*- coding: utf-8 -*-
#- Modificar el ejercicio anterior generando que únicamente sume números que sean múltiplos de 3, 5 o 7 hasta el número ingresado.


numero=int(input("Ingrese un numero positivo: "))
#Agregando el int() pasamos un string a int
#print(type(numero))

sumatoria=0
for x in range (numero,0,-1):
    if(x % 3 == 0 or x % 5 == 0 or x % 7 == 0):
        sumatoria+=x
print (sumatoria)
