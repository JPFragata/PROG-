# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 08:22:48 2024

@author: PC14
"""

#LISTA DE FIXAÇÃO DE TUPLAS


# 2A --------------------------------
def recebeString(s):
    maior=s[0]
    cont=0
    for letra in s:
        if letra>maior:
            maior=letra
    for letra in s:
        if letra==maior:
            cont+=1
    return (maior,cont)

resp=recebeString('baboseirasssss')
print(resp)   

# 2B --------------------------------

def minmax(lista):
    maior=lista[0]
    menor=lista[0]
    contMaior=0
    contMenor=0
    for item in lista:
        if item>maior:
            maior=item        
        if item<menor:
            menor=item
    for item in lista:
        if item == maior:
            contMaior+=1 
        if item == menor:
            contMenor+=1 
    return ((menor,contMenor),(maior,contMaior))

lista=[1,3,2,5.3,1,78,5,8,6,8,5]

# 4 ----------------------------------


    
