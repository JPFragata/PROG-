# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:29:17 2024

@author: jpfragata
"""

from classeFRACAO import *


#QUESTÃO 01 -------------------------

# Um livro tem 132 páginas. Leda já leu 7/11 desse livro. Quantas páginas ela já 
# leu desse livro?

total_paginas = 132
fracao_lida = Fracao(7,11)
paginas_lidas = (fracao_lida.getNum()/fracao_lida.getDen()) * total_paginas
print('QUESTÃO 01:\nEla leu ao todo {} páginas'.format(int(paginas_lidas)))

#QUESTÃO 02 --------------------------

# Uma escola tem 54 professores. Desses, 5/9 são do sexo feminino. Quantas 
# professoras há nessa escola?

total_professores = 54
fracao_feminino = Fracao(5,9)
qtd_professoras = (fracao_feminino.getNum()/fracao_feminino.getDen()) * total_professores
print('\nQUESTÃO 02:\nTêm {} professoras na escola'.format(int(qtd_professoras)))

#QUESTÃO 03 --------------------------

# Em uma corrida de fórmula 1, 26 carros iniciaram a corrida. Desses carros, 4/13 
# abandonaram a corrida por defeitos mecânicos. Quantos carros terminaram a corrida?

total_carros = 26
desistentes = Fracao(4,13)
fracao_restantes = 1 - (desistentes.getNum()/desistentes.getDen())
restantes = total_carros*fracao_restantes
print('\nQUESTÃO 04:\n{} carros permaneceram na corrida'.format(int(restantes)))

#QUESTÃO 04 --------------------------

# O mostrador de gasolina de um carro mostra que o tanque está cheio até os seus 
# ¾. Se o tanque está com 48 litros de gasolina, quantos cabem, ao todo, no tanque 
# desse carro?

tanque_atual = 48
fracao = Fracao(3,4)


































