# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:08:14 2022

@author: elena
"""
'''
Ejercicio 3
Dadas dos listas, debes generar una tercera con todos los elementos que se 
repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
'''


lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

lista_3 = []
for i in lista_1:
    if i in lista_2:
        lista_3.append(i)


listfinal = []
for i in lista_3:
    if i not in listfinal:
        listfinal.append(i)
    
        
print(listfinal)




