# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 08:17:20 2024

@author: PC14
"""


# #1.	Considere os seguintes dicionários:
dAlunosTurmas = {
     'Ana':'33A',
     'Patinhas':'33A',
     'Zé':'33A',
     'Pedro':'33C',
     'Carla':'33B',
     'So':'33B', 
     'Margarida':'33A',
     'Donald':'33B',
     'Lola':'33C',
     'Carlos':'33A',
     'Maios':'33G'
 }

dTurmasLabProvas = {
     '33A': 'L258',
     '33B': 'L270',
     '33C': 'L314',
     '33G': 'L258'
 }    

# a) Construa uma função que 
#     receba estes dicionários e o nome de um aluno e 
#     mostre para este aluno qual sua sala de prova

def exibeSalaDeProva(dAlunosTurmas,dTurmasLabProvas,nome):
    turma = dAlunosTurmas.get(nome,'inex')
    if turma != 'inex':
        sala_prova = dTurmasLabProvas.get(turma,'inex')
        print(sala_prova)
    else:
        print('Aluno não matriculado')
        


# b)	Construa uma função que 
#     receba estes dicionários e 
#     construa umbnovo dicionário onde :
#           chave: aluno
#           valor: sala de prova

def constroiDicChaveAluno(dAlunosTurmas,dTurmasLabProvas):
    dicAlunoSala = {}
    for (nome,turma) in dAlunosTurmas.items():
        sala = dTurmasLabProvas.get(turma,'inex')
        if sala != 'inex':
            dicAlunoSala[nome] = sala
    return dicAlunoSala
            






# c) Construa uma função que 
#     receba o dicionário do item b) e 
#     construa um novo dicionário cuja 
#         a chave é o laboratório e 
#         o valor é a quantidade de alunos que farão prova neste laboratório (dicionário de frequências)








# d) Construa uma função que 
#     receba o dicionário do item b) e 
#     construa um novo dicionário cuja 
#         a chave é a sala e 
#         o valor é uma lista do nome dos alunos que farão prova neste laboratório ( dicionário de agrupamentos)







# e) Construa uma função que 
#     receba dAlunosTurmas   e 
#     construa o dicionário dTurmasAlunos, 
#         onde a chave é a turma e 
#         o valor é a lista de alunos desta turma. (dicionário inverso)






        
# f) Utilizando o dicionário dTurmasAlunos ( chave: Turma, valor: lista de alunos) 
#     construa o dicionário dLabComTurmas 
#         onde a chave é o laboratório e 
#         o valor é o dicionário dTurmasAlunos
#             dLabComTurmas--> {
#                 'L258’ : {'33A’ : [   'Patinhas',  'Zé', 'Margarida', 'Carlos'] , ‘33G’:[‘Maios’] },
# 	 'L270' :  {'33B’ : [   'Carla',  'So', 'Donald']},
# 	 'L314' :  {'33C’ : [   'Pedro',  'Lola']}
# 	     }








# g) Construa uma função que receba dTurmasLabProvas e 
#   retorne um novo dicionário, onde 
#                chave: lab e 
#                valor: lista de turmas do lab