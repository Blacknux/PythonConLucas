# -*- coding: utf-8 -*-
#===============================================================================
# 2.3 Listas por comprenci�n:
# 
# - Dado una lista de n�meros enteros definir una nueva lista que indica la tupla numero-paridad(true/false)
# - Dado una lista de n�meros de 0 a 100 obtener los n�meros que esten por debajo de 50.
# - Dado una lista de n�meros de 0 a 100 obtener los n�meros que esten por debajo de 50 tal cual estan y los que no deber�n ser multiplicados por 2.
# - Dado un n�mero N entero entregar un generador que recorra todos los n�meros pares <= a N.
#===============================================================================

def GenList(cant):
    list = []
    for x in range(cant+1):
        list.append(x)
    return list

def TuplaParidad(lista):
    auxi=[]
    for x in lista:
        if (x%2==0):
            auxi.append(x)
    tupla=(auxi)
    return tupla
   
def TuplaParidad2(lista):
    auxi={}
    for x in lista:
        if (x%2==0):
            #data={x:"True"}
            auxi.update({x:"True"})
        else:
            auxi.update({x:"False"})
    
    return auxi 

def TuplaParidad3(lista):
    auxi=[]
    for x in lista:
        if (x%2==0):
            #data={x:"True"}
            auxi.append((x,"True"))
        else:
            auxi.append((x,"False"))
    
    return auxi 

def Menoresa50(list):
    less50=[]
    for iter in list:
        if(iter < 50):
            less50.append(iter)
    return less50
def Men50MayX2(list):
    newList=[]
    for iter in list:
        if(iter < 50):
            newList.append(iter)
        elif(iter>=50):
            newList.append(iter*2)
    return newList
def paresHastaN(numero):
    auxi=[]
    for x in range (numero):
        if (x%2==0 and x!=0):
            auxi.append(x)
    tupla=(auxi)
    return tupla            
    
            
def PrintList(list):
    newList=""
    for x in list:
        newList+= str(x)+","
        
    print(newList)
    
    
print(TuplaParidad3(GenList(10)))
    #print(paresHastaN(20))

    
