# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 07:34:38 2024

@author: PC14
"""

class ContaUsuario:                                 #como construir um objeto desta classe
    def __init__(self,login,senha='123'):           #caso não tenha senha, a criada de padrão será '123' (default)
        self.login=login
        self.senha=senha                    
        self.ativa=False                            #A conta sempre nascerá inativa segundo o enunciado. Não pode ser instanciado, pois DEVE nascer inativa
    
    def __str__(self):                              #usado pelo 'print'
        if self.ativa:
            resp='Ativa'
        else:
            resp='Inativa'
        return f'Login:{self.login} Status:{resp}'
        
    def __repr__(self):
        return f'Login:{self.login} Status:{self.ativa}'
        
    def alteraStatus(self):
        self.ativa=not self.ativo                   #Se é verdadeira, fica falsa. Se está falsa, fica verdadeira
        
    def alteraSenha(self,nova_senha):
        self.senha=nova_senha
    
# PARA IMPORTAR, ASSIM COMO ARQUIVOS, O DOCUMENTO QUE CONTÉM A CLASSE DEVE ESTAR NA MESMA PASTA QUE 
# O ARQUIVO ONDE SERÁ IMPORTADA
        
        
        