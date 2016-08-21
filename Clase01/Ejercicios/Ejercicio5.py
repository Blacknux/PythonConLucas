# -*- coding: utf-8 -*-
#- Escribir un programa que reciba un número entero positivo, devolver la sumatoria de dicho número.

numero=int(input("Ingrese un numero positivo: "))

print(type(numero))

sumatoria=0
for x in range (numero,0,-1):
    sumatoria+=x
print (sumatoria)
