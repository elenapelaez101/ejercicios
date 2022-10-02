# -*- coding: utf-8 -*-
"""
Ejercicio 5

Crea un script llamado descomposicion.py que realice las siguientes tareas:
Debe tomar 1 argumento que será un número entero positivo.
En caso de no recibir un argumento, debe mostrar información acerca de cómo 
utilizar el script.

El objetivo del script es descomponer el número en unidades, decenas, centenas, 
miles... tal que por ejemplo si se introduce el número 3647:
python descomposicion.py 3647

El programa deberá devolver una descomposición línea a línea como la siguiente 
utilizando las técnicas de formateo:
0007
0040
0600
3000

Pista
Que el valor sea un número no significa necesariamente que deba serlo para 
formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas 
conversiones entre tipos cadenas, números y viceversa
"""

print('hola')
while True:
    numero = input('Dígame el número entero y positivo que desee: ')

    try:
        int(numero)
        break
    
    except ValueError:
        print('Si quiere que el programa funcione debe introducir un número entero y positivo y se lo descompondremos en decenas, decenas...')
        continue
    
    

numlis= list(str(numero))
ceros = []
for i in numlis:
    ceros.append(0)
    
print(' ')

for i in reversed(range(len(numlis))):
    ceros[i]=numlis[i]
    
    c= [str(j) for j in ceros]
    limpio = str("".join(c))
    print(limpio)
    ceros[i] = 0

    
    
    
    
    
    
    
    
    
    
    
    