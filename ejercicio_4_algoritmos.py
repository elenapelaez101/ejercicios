# -*- coding: utf-8 -*-
"""
Ejercicio 4
Durante la planificación de un proyecto se han acordado una lista de tareas. 
Para cada una de estas tareas se ha asignado un orden de prioridad 
(cuanto menor es el número de orden, más prioridad).

¿Eres capaz de crear una estructura del tipo cola con todas las tareas 
ordenadas pero sin los números de orden?
Sugerencia

Para ordenar automáticamente una lista es posible utilizar el método .sort(), 
deberias probarlo.
"""

tareas = {1:'modelar',5:'pintar',3:'cortar',2:'obtener materiales',4:'fabricar'}
prioridad =list(tareas.keys())

prioridad.sort()
tareasord =[]
for i in prioridad:
    if i in tareas.keys():
        tareasord.append(tareas[i])
        
print(tareasord)
