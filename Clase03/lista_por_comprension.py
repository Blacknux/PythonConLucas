'''
Created on 3 sep. 2016

me 

@author: python
'''
from builtins import *

class auto():
    ruedas=4
    
    def __init__(self, marca1):
        self.marca=marca1; 
        self.marcha=False  
    
    def arrancar(self):
        if(self.marcha == False):
            print("rummmm rummmm",self.marca)
            self.marcha=True
        else:
            print("Ya esta prendido")
        
    def apagar(self):
        if(self.marcha ==True):
            print("Se apago el auto marca",self.marca)
            self.marcha=False
        else:
            print("El auto no esta encendido")
            prender=input("queres prenderlo??,1-si 2-no")
            if(prender=="1"):
                self.arrancar()
            else:
                pass
     

class cuatriciclo(auto):
    pass       
   

tuauto=auto("ferrari")
tuauto.apagar()
tuauto.arrancar()
tuauto.apagar()

