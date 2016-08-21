# -*- coding: utf-8 -*-
#- Escribir un programa que reciba texto, si es una fruta y es una banana o manzana indica "yummi", si no lo es dice "puajjj"

frutas=["banana","manzana"]
alimento=input("Ingrese un alimento ")

if(alimento in frutas):
    print ("Yummi")
else:
    print("Puaj")