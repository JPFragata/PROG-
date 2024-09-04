# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 08:39:16 2024

@author: PC14
"""

#Considere os seguintes dicionários:

- dicProjetoEParticipantes: dicionário com as horas trabalhadas pelos participantes
    dos projetos onde
        chave: nome do projeto
        valor: lista de tuplinhas com 
                 (nome da pessoa , horas trabalhadas) 
               dos participantes do projeto
    Ex: 'Praia Limpa': [('Elzira',5),('Lia',6)],
        a Elzira trabalhou 5 hs no projeto Praia Limpa e 
        a Lia, 6 horas 
        
dicSecretariaEProjetos= dicionário com os projetos de cada secretaria onde
        chave: nome da secretaria responsável pelos projetos
        valor: lista de projetos
   Ex: {'Meio Ambiente': ['Mundo Verde', 'SOS Planeta', 'Praia Limpa'], 
        os projetos Mundo Verde', 'SOS Planeta' e 'Praia Limpa são de responsabilidade
        da secretaria do Meio Ambiente
        
 
        
"""


"""
Invertendo o dicionário participantes por projeto

Construir um dicionário de ProjHorasPorParticipante
    chave: Participante
    valor: dicionário interno onde a 
              chave: projeto
              valor: qt de horas trabalhadas no projeto
              
              
              
Dicionário Original:
    {'Mundo Verde': [('Elzira',10),('Ernesto',6)],
     'Casa Inteligente': [('Elzira',8),('Carla',7)],
     'SOS Planeta': [('Marcia',10),('Lia',10),('Kiko',5)],
     'Cidade Limpa': [('Lala',20)],
     'Praia Limpa': [('Elzira',5),('Lia',10)],
     'Cultura para Todos': [('Ernesto',10),('Lala',5)],
     'Biblioteca Volante': [('Carla',8),('Marcia',10),('Lia',10)]}
    
Dicionário Invertido: diconário de dicionários
    {'Elzira': {'Mundo Verde': 10, 'Casa Inteligente': 8, 'Praia Limpa': 5}, 
     'Ernesto': {'Mundo Verde': 6, 'Cultura para Todos': 10}, 
     'Carla': {'Casa Inteligente': 7, 'Biblioteca Volante': 8}, 
     'Marcia': {'SOS Planeta': 10, 'Biblioteca Volante': 10}, 
     'Lia': {'SOS Planeta': 10, 'Praia Limpa': 10, 'Biblioteca Volante': 10}, 
     'Kiko': {'SOS Planeta': 5}, 
     'Lala': {'Cidade Limpa': 20, 'Cultura para Todos': 5}}          
   
               
"""

    

"""
Juntando os dicionários dicSecretariaEProjetos e dicProjetoEParticipantes

Construir um dicionário de ProjetosEParticipantesPorSecretaria
    chave: secrectaria
    valor: dicionário interno onde a 
              chave: projeto
              valor: lista de participantes do projeto (nome,valor)
              
Dicionários Originais:
    dicSecretariaEProjetos={'Meio Ambiente': ['Mundo Verde', 'SOS Planeta', 'Praia Limpa'],
                         'Infraestrutura': ['Casa Inteligente'],
                         'Conservação': ['Cidade Limpa'], 
                         'Educação': ['Cultura para Todos', 'Biblioteca Volante']}   

     dicProjetoEParticipantes={'Mundo Verde': [('Elzira',10),('Ernesto',6)],
                           'Casa Inteligente': [('Elzira',8),('Carla',7)],
                           'SOS Planeta': [('Marcia',10),('Lia',10),('Kiko',5)],
                           'Cidade Limpa': [('Lala',20)],
                           'Praia Limpa': [('Elzira',5),('Lia',10)],
                           'Cultura para Todos': [('Ernesto',10),('Lala',5)],
                           'Biblioteca Volante': [('Carla',8),('Marcia',10),('Lia',10)]}

     
    
Dicionário de Dicionários resultante
              
    {'Meio Ambiente': {'Mundo Verde': [('Elzira', 10), ('Ernesto', 6)], 
                       'SOS Planeta': [('Marcia', 10), ('Lia', 10), ('Kiko', 5)], 
                       'Praia Limpa': [('Elzira', 5), ('Lia', 10)]}, 
     'Infraestrutura': {'Casa Inteligente': [('Elzira', 8), ('Carla', 7)]},
     'Conservação': {'Cidade Limpa': [('Lala', 20)]}, 
     'Educação': {'Cultura para Todos': [('Ernesto', 10), ('Lala', 5)], 
                  'Biblioteca Volante': [('Carla', 8), ('Marcia', 10), ('Lia', 10)]}}
      
        
"""
#def inverteDicionarioProjetoEParticipantes(dicProjetoEParticipantes):
    
    

#def constroiDicProjetosEParticipantesPorSecretaria(dicSecretariaEProjetos,dicProjetoEEquipe):


dicProjetoEParticipantes={'Mundo Verde': [('Elzira',10),('Ernesto',6)],
                          'Casa Inteligente': [('Elzira',8),('Carla',7)],
                          'SOS Planeta': [('Marcia',10),('Lia',10),('Kiko',5)],
                          'Cidade Limpa': [('Lala',20)],
                          'Praia Limpa': [('Elzira',5),('Lia',10)],
                          'Cultura para Todos': [('Ernesto',10),('Lala',5)],
                          'Biblioteca Volante': [('Carla',8),('Marcia',10),('Lia',10)]}

dicSecretariaEProjetos={'Meio Ambiente': ['Mundo Verde', 'SOS Planeta', 'Praia Limpa'],
                        'Infraestrutura': ['Casa Inteligente'],
                        'Conservação': ['Cidade Limpa'], 
                        'Educação': ['Cultura para Todos', 'Biblioteca Volante']}


#dProjHoraPorPartic=inverteDicionarioProjetoEParticipantes(dicProjetoEParticipantes)
#print("\nDicionário Invertido: Projetos e Horas por Participante:")
#print(dProjHoraPorPartic)


#dProjEquipPorSec=constroiDicProjetosEParticipantesPorSecretaria(dicSecretariaEProjetos,dicProjetoEParticipantes)
#print("\nProjetos e Participantes por Secertaria:\n")
#print(dProjEquipPorSec)