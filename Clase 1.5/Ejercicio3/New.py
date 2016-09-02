'''
Created on 27 ago. 2016

@author: Knux
'''
from sre_parse import isdigit



def nuevoAlumno():
    nombre=input("Nombre Alumno: ")
   
    nota=[]
    for x in range(3):
        notaAux=int(input("Nota Alumno %s: "%nombre))
        while(notaAux < 0 or notaAux > 10 or not isdigit(str(notaAux)) ):
            notaAux=int(input("Error la nota debe ser entre 0 y 10 y solo numero\nNota Alumno %s: "%nombre))
        nota.append(str(notaAux))
    Alumno={nombre:nota}
    return Alumno

    
def nuevaMateria(nombre):
    print("Toda materia para abrirse necesita al menos un alumno, por favor registre uno\n")
    materia={nombre:nuevoAlumno()}
    return materia
    
    