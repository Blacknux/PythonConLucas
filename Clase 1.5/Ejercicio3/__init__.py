'''
Created on 27 ago. 2016

@author: Knux
'''
from New import *
from sre_parse import isdigit
from os import system

opcion=55
materias={}
while (opcion!=8):
    opcion=int(input("1-Agregar Materia\n2-Agregar Alumno y nota\n3-Ver notas\n8-Salir"))
    if(opcion==1):
        nombreMat = input("Codigo de Materia: ")
        while(len(nombreMat) != 5 or not isdigit(nombreMat)):
           nombreMat=input("Codigo de  Materia: ")
        materia = nuevaMateria(nombreMat)
        materias.update(materia)
        
    elif(opcion==2):
        if(len(materias)==0):
            pass
        else:
            print("Las materias registradas son:")
            for val in materias:
                print(val)
                
            nombreMat=input("En que materia desea registrar el alumno?\nNumero Mat: ")
            while(nombreMat not in materias):
                print("Materia inexistente\nLas materias registradas son:")
                for val in materias:
                    print(val)
                nombreMat=input("En que materia desea registrar el alumno?\nNumero Mat: ")
                
            materiaAux=materias[nombreMat]
            materiaAux.update(nuevoAlumno())
        
    elif(opcion==3):
        if(len(materias)==0):
            pass
        else:
              
            codigo=input("Ingrese el codigo de la materia: ")
            while(codigo not in materias ):
                codigo=input("Materia no valida\nIngrese el codigo de la materia o (exit para salir): ")
                if(codigo =="exit"):
                    break
            if(codigo != "exit"): 
                alumno=input("Ingrese el Key del alumno: ")
                while(alumno not in materias[codigo] ):
                    alumno=input("Alumno no Esistente\nIngrese el codigo de la materia o (exit para salir): ")
                    if(alumno =="exit"):
                        break
                if(alumno!="exit"):
                    for iter in materias[codigo][alumno]:
                        print(iter)
        
#        
        
        
       
            