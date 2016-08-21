# -*- coding: utf-8 -*-
#¿Que año es dentro de 20 años?
import datetime

ahora=datetime.datetime.now()
anio=ahora.year
print("Hoy es el anio: "+str(anio))
en20anios=ahora.year + 20

print ("En 20 anios sera el anio: "+str(en20anios))

