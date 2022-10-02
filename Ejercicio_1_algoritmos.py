# -*- coding: utf-8 -*-

'''
Ejercicio 1
Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés.
 Al parecer contiene el nombre de un alumno y la nota de un exámen.
¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
Nombre Apellido ha sacado un Nota de nota.
Ayuda
Para voltear una cadena rápidamente utilizando slicing podemos 
utilizar un tercer índice -1: cadena[::-1]
cadena = "zeréP nauJ,01"
'''


def voltear(cad):
    volteada = cad[::-1]
    nota = volteada.split(',')[0]
    nombre = volteada.split(',')[1]
    print (nombre+' ha sacado un '+nota+' de nota.')
    
    
voltear("zeréP nauJ,01")


























