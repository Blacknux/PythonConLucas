'''
Created on 28 ago. 2016

@author: Knux
'''
def esPrimo(numero):
    flag = 0
    for x in range (numero+1,0,-1):
        if(numero%numero-1==0):
            flag+=1
        #=======================================================================
        # if(flag>2):
        #     break
        #=======================================================================
    if(flag<2):
        print("%d Es primo"%numero)
    else:
        print("%d NO es primo"%numero)
        
esPrimo(8)