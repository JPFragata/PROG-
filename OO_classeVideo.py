# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 08:27:22 2024

@author: PC14
"""


class Video:
    def __init__(self,nome,duracao,tema='Python',ano='2020'):
        self.nome=nome
        self.tema=tema
        self.ano=ano
        self.duracao=duracao
        self.qtlike=0
        self.qtUnlike=0
        
    def __str__(self):
        return f'Nome:{self.nome}, Tema:{self.tema}, Ano:{self.ano}, Duração:{self.duracao}, Likes:{self.qtLikes}, Unlikes:{self.qtUnlikes}'
    
    def __repr__(self):
        return f'Nome:{self.nome}, Tema:{self.tema}, Ano:{self.ano}, Duração:{self.duracao}, Likes:{self.qtLikes}, Unlikes:{self.qtUnlikes}'
        
    def __add__(self,outro):
        novo_nome = self.nome+'&'+outro.nome
        novo_tema = self.tema+'&'+outro.tema
        