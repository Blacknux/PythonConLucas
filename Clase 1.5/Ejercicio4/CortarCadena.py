'''
Created on 28 ago. 2016

@author: Knux
'''
def PedirCadena():
    cadena=input("Ingrese una cadena entre 10 y 20 chars: ")
    while(len(cadena)<10 or len(cadena)>20):
        cadena=input("Error largo no valido\n\nIngrese una cadena entre 10 y 20 chars: ")
    
    return cadena
    
def CortarCadena(stringg):
    newString=stringg
    newString=newString[:3]+newString[len(newString)-5:]
    return newString

def MostrarString(string):
    print(string)
    
if __name__=="__main__":
    MostrarString(CortarCadena(PedirCadena()))
    