'''
Created on 27 ago. 2016

@author: Nahuel Claret
'''

class Alumno():
    
    def __init__(self,name,note):
        self.nombre=name
        self.nota=note
    
    
    
if __name__ == "__main__":
    alumnos=[]
    acumulador=0
    for x in range(5):
        nombre=input("Nombre: ")
        while (len(nombre)<5):
            nombre=input("Error 5 letras minimo\nIngrese el nombre: ")
        nota=int(input("Nota: "))
        while(nota <0 or nota > 10):
            nota=int(input("Error la nota debe ser entre 0 y 10\nNota: "))
            
        newalumn= Alumno(nombre,nota)
        alumnos.append(newalumn)
    
    for x in alumnos:
        nameAlumno=x
        acumulador+=nameAlumno.nota
    
    print("el promedio es :",acumulador/len(alumnos))
        
