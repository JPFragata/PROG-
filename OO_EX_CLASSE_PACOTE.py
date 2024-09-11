# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 08:45:14 2024

@author: PC14
"""

#Baseado em questão de profa Joisa

# A classe Pacote serve para representar pacotes de uma transportadora
# larg, altura, prof em cm

# CONSULTE OS MÉTODOS MÁGICOS DOS SLIDES e complete a classe Pacote 
# de modo que o codigo da parte principal resulte na saida apresentada 
# ao final.

# Dica Importante: os metodos para operacoes +, -, *, / devem retornar 
# um novo pacote, enquanto os metodos para atribuicao composta +=, -=,
#  *=, /= devem alterar atributo(s) do proprio objeto e retornar uma 
# referencia para o proprio objeto (ou seja, retornar self )

# Um pacote quando criado tem larg,alt,prof e destino com valor default "A definir"
# Na exibição os atributos, alt,larg e prof devem ser exibidos
# Ao somar dois pacotes, um novo pacote é criado com a soma das dimensões
# Ao somar um valor ao pacote, este valor é somado às suas dimensões
# Métodos para alterar e recuperar seu atributos
# Método para calcular o volume
# Métodos para comparações de pacotes:
#      ==: mesmas dimensões
#      <: comparação em relação ao volume. Pacotes com mesmo volume: decidir pela altura
     
#                       
#----------------------- Definição da classe Pacote --------------------------





    
#fim da classe Pacote
#-----------------------------------------------------------------    
#PARTE PRINCIPAL: retire os #    
# pac1= Pacote(30,20,10,'Joe')    
# print(pac1)
# pac2= Pacote(25,20,32)
# print(pac2)
# print('VOLUME: {} cm3'.format(pac1.volume()))
# print('VOLUME: {} cm3'.format(pac2.volume()))
# pac3= pac1+pac2   
# print(pac3)
# pac1+=3
# print(pac1)

# pac2.setDestinatario('LALA')
# print(pac2)
# print("Pac1 {} - volume: {} - Pac2 {} - volume {}".format(pac1,pac1.volume(),pac2,pac2.volume()))
# if pac1<pac2:
    
#     print("menor: ", pac1)
# else:
#     print("menor: ", pac2)


'''
SAIDA ESPERADA:
Pacote com LARG:30.0, ALT:20.0, PROF:10.0 para Joe
Pacote com LARG:25.0, ALT:20.0, PROF:32.0 para A definir
VOLUME: 6000 cm3
VOLUME: 16000 cm3
Pacote com LARG:55.0, ALT:40.0, PROF:42.0 para A definir
Pacote com LARG:33.0, ALT:23.0, PROF:13.0 para Joe
Pacote com LARG:25.0, ALT:20.0, PROF:32.0 para LALA
Pac1 Pacote com LARG:33.0, ALT:23.0, PROF:13.0 para Joe - volume: 9867 - Pac2 Pacote com LARG:25.0, ALT:20.0, PROF:32.0 para LALA - volume 16000
menor:  Pacote com LARG:33.0, ALT:23.0, PROF:13.0 para Joe'''
    



