# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 20:07:14 2023

@author: Ferlin
"""

t1=([2,3],4,'meio',('a',))
#in
# 2 in t1
# ('a',) in t1
# 'meio' in t1
# 'a' in t1


#len(t1)

#*
# t1r=t1=([2,3],4)
# t1*3

#+
# t1s=([2,3],4)
# t2s=(5,'seis',7)
# t1+t2

#fatiamento
# t2=(10,20,30,40,50)
# t1[2:4]
# t1[2:]
# t1[:4]
# t1[:]
# t1[::-1]
# t1[3::-1]
# t1[3::-2]


#atribuição múltipla
# tupla de variáveis = tupla de valores
# n1=4
# n2=3
# t1=(n1,n2)
# (n2,n1)=t1

#criando uma tupla iterativamente
# tupla é imutável, para criá-la dinamicamente:
    # 1) cria uma lista vazia e inclui elementos na lista
    # 2) torna a lista uma tupla
    
import random

def cria_tupla(n):
    l=[]
    for i in range(n):
        l.append(random.randint(10,30))
    return tuple(l)