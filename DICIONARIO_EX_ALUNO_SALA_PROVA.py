# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 08:23:24 2024

@author: PC18
"""


Considere os seguintes dicionários:

    Dicionário dAlunosTurmas: Mapeia o nome dos alunos para suas respectivas turmas.
    Exemplo: 'Ana': '33A' indica que a aluna Ana está na turma 33A.

    Dicionário dTurmasLabProvas: Mapeia as turmas para os laboratórios onde as provas serão realizadas.
    Exemplo: '33A': 'L258' indica que a turma 33A fará a prova no laboratório L258.
    
a)	Construa a função mostrar_sala_prova que receba estes dicionários, e o nome de um aluno e
    mostre para este aluno qual sua sala de prova ou ua mensagem caso o aluno
    não esteja no dicionário

b)	Construa a função construir_dicionario_frequencias que receba estes dicionários
    e construa um novo dicionário que contará quantos alunos estão alocados 
    para cada laboratório. O novo dicionário tem como:
         chave é o laboratório e o 
         valor é a quantidade de alunos que farão prova neste laboratório (dicionário de frequências)
'''

dAlunosTurmas = {'Ana':'33A',
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

dTurmasLabProvas = {'33A': 'L258',
        '33B': 'L270',
        '33C': 'L314',
	'33G': 'L258'
}    


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

# ------------------------------RESOLUÇÃO-----------------------------------------------
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
        
# -----------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
# c) Construa uma função que 
#     receba o dicionário do item b) e 
#     construa um novo dicionário cuja 
#         a chave é o laboratório e 
#         o valor é a quantidade de alunos que farão prova neste laboratório (dicionário de frequências)


def constroiDicLabQtd(dAlunosTurmas,dTurmasLabProvas):
    dicLabQtd ={}
    for (nome,lab) in constroiDicChaveAluno(dAlunosTurmas,dTurmasLabProvas).items():         #PARA CADA TUPLA COM (NOME, LAB) NO DICIONÁRIO RECEBIDO
        qtd = dicLabQtd.get(lab,0)                                                           #QUANTIDADE RECEBE 0, POIS ELE NÃO ENCONTRA O 'LAB' NO DICIONÁRIO EM CRIAÇÃO
        qtd += 1                                                                             #ADICIONA 1 PESSOA NA QUANTIDADE
        dicLabQtd[lab] = qtd                                                                 #ADICIONA AO DICIONÁRIO {'LAB' : QTD}
    return dicLabQtd                                                                         #RETORNA O DICIONÁRIO

# -----------------------------------------------------------------------------
# d) Construa uma função que 
#     receba o dicionário do item b) e 
#     construa um novo dicionário cuja 
#         a chave é a sala e 
#         o valor é uma lista do nome dos alunos que farão prova neste laboratório ( dicionário de agrupamentos)


def constroiDicSalaListaAlunos(dAlunosTurmas,dTurmasLabProvas):
    dicAgrupamento = {}
    dicAlunoSala = constroiDicChaveAluno(dAlunosTurmas, dTurmasLabProvas)
    for (aluno,lab) in dicAlunoSala.items():
        lAlunos_lab = dicAgrupamento.get(lab,[])
        lAlunos_lab.append(aluno)
        dicAgrupamento[lab] = lAlunos_lab
    return dicAgrupamento
        
# -----------------------------------------------------------------------------
# e) Construa uma função que 
#     receba dAlunosTurmas   e 
#     construa o dicionário dTurmasAlunos, 
#         onde a chave é a turma e 
#         o valor é a lista de alunos desta turma. (dicionário inverso)

def inverteDicionario(dAlunosTurmas):
    dTurmasAlunos = {}
    for (aluno,turma) in dAlunosTurmas.items():
        lAlunos_turma = dTurmasAlunos.get(turma,[])
        lAlunos_turma.append(aluno)
        dTurmasAlunos[turma] = lAlunos_turma
    return dTurmasAlunos
        
# -----------------------------------------------------------------------------       
# f) Utilizando o dicionário dTurmasAlunos ( chave: Turma, valor: lista de alunos) 
#     construa o dicionário dLabComTurmas 
#         onde a chave é o laboratório e 
#         o valor é o dicionário dTurmasAlunos
#             dLabComTurmas--> {
#                 'L258’ : {'33A’ : [   'Patinhas',  'Zé', 'Margarida', 'Carlos'] , ‘33G’:[‘Maios’] },
# 	 'L270' :  {'33B’ : [   'Carla',  'So', 'Donald']},
# 	 'L314' :  {'33C’ : [   'Pedro',  'Lola']}
# 	     }

def constroiDicLabComTurmas(dTurmasLabProvas):
    dicDeDic = {}
    dTurmasAlunos = inverteDicionario(dAlunosTurmas)
    for (turma,sala) in dTurmasLabProvas.items():
        if sala not in dicDeDic:
            dicDeDic[sala] = {}
        if turma in dTurmasAlunos:
            dicDeDic[sala][turma] = dTurmasAlunos[turma]
    return dicDeDic
    
#ESTÁ COLOCANDO APENAS A TURMA 33G, POIS ESTA ESTÁ SOBRESCREVENDO A 33A

# -----------------------------------------------------------------------------
# g) Construa uma função que receba dTurmasLabProvas e 
#   retorne um novo dicionário, onde 
#                chave: lab e 
#                valor: lista de turmas do lab

def dicLabComListadeTurma(dTurmasLabProvas):
    dicAgrupamento = {}
    for (turma,lab) in dTurmasLabProvas.items():
        lTurmasLab = dicAgrupamento.get(lab,[])
        lTurmasLab.append(turma)
        dicAgrupamento[lab] = lTurmasLab
    return dicAgrupamento  
