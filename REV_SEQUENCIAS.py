# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 07:40:23 2024

@author: PC14
"""

#                           REVISÃO DE SEQUÊNCIAS
def criaListaDeTexto(seq):
    texto=seq
    lista=list(texto)
    return lista



# LISTA DE REVISÃO DE SEQUÊNCIAS ---------------------------------------------

#QUESTÃO 01

#LETRA A

L=[10,-10,3,89,34,-66,23,9,89,12,23,34,-11,20,31,89,20]

def qualMaior(lista):
    maior=lista[0]      #NÃO PODE COLOCAR MAIOR=0, POIS POSSUI VALORES NEGATIVOS NESSA LISTA
    for item in lista:
        if item > maior:
            maior=item
    return maior
        
#LETRA B

def ondeMaior(lista):
    maior=qualMaior(lista)
    for (pos,valor) in enumerate(lista):
        

#LETRA C

def ondeTodosMaior(lista):
    l=[]
    maior=qualMaior(lista)
    for (pos,valor) in enumerate(lista):
        if valor==:
            l.append(pos)
    return l 
            
#LETRA D

def somaOutros(lista):
    soma=0
    maior=qualMaior(lista)
    for item in lista:
        if item != maior:
            soma+=item
    return soma

#LETRA E 

def somaPosteriores(lista):
    soma=0
    posSucessor=ondeMaior(lista)+1
    for item in lista[posSucessor::]:
        soma+=item
    return soma
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    