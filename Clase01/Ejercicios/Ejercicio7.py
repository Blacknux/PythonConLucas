# -*- coding: utf-8 -*-
#- Dado un numero ingresado por el usuario, dar la posibilidad al mismo de: generar su sumatoria o su factorial.


def Sumatoria(numero):
    sumatoria=0
    for x in range (numero,0,-1):
        sumatoria+=x
    print ("La sumatoria de "+str(numero)+" es %d"%sumatoria)

def Factorial(numero):
    factorial=1
    for x in range (numero,0,-1):
        factorial = factorial * x
    print ("El factorial de "+str(numero)+" es %d"%factorial)

def main():

    numero=int(input("Ingese un numero: "))
    opcion=input("El numero elejido es:%d \nSeleciones si desa sacar\n1-Sumatoria\n2-Factorial "%numero)

    if (opcion=="1"):
        Sumatoria(numero)
    elif(opcion=="2"):
        Factorial(numero)
    else:
        print ("Opcion invalida")
        main()

main()