# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 07:50:31 2024

@author: PC14
"""


# Considere um dicionário de dicionário em que cada elemento é:
    
#     CHAVE: matrícula do ALUNO
#     VALOR dicionário com disciplinas cursadas e respectivas notas
  
# Exemplo de um elemento desse dicionário:
    
#    '1413399': {'ENG1000': 8.4, 'MAT1161': 9.2, 'MAT1260': 5.3} 



# 1) Escreva uma função, denominada exibeNotaNaDisc, que:
# - receba um dicionário como o descrito, um aluno (mat) e
# uma disciplina
# - exiba a nota do aluno na disciplina
# OBS: lembrar que o aluno pode não estar no dic externo ou pode 
# não ter cursado a disciplina. Exibir a msg aprodpriada para cada caso.


def exibeNotaNaDisc(dicMatdDiscNota, aluno, disc):
    info_aluno = dicMatdDiscNota.get(aluno,print('Aluno não encontrado'))
    if info_aluno:
        nota = info_aluno.get(disc,print('aluno não matriculado'))
        if nota:
            print(f'aluno {aluno} tirou nota {nota} na disciplina {disc}')           
    

# 2) Escreva uma função que receba o dicionaário descrito e 
# retorne um dicionário de diconários por DISCIPLINA, em 
# que cada item do dic é:
#     CHAVE: disciplina
#     VALOR: dicionário com os alunos que cursaram a disciplina e 
#     suas respectivas notas
    

#     FIS1033 : {'1612299': 5.7, '1511188': 8.7, '1412222': 6.8, 
#                '1418833': 6.1, '1414466': 9.4, '1312211': 6.7, 
#                '1713300': 6.4, '1417700': 8.6}
     
def criaDicAlNtDaDisc(dicMatdDiscNota):
    dicNovoInv = {}
    for (aluno,dicInterno) in dicMatdDiscNota.items():  
        for (disc,nota) in dicInterno.items():
            dicInterno = dicNovoInv.get(disc,{})
            dicInterno[aluno] = nota
            dicNovoInv[disc] = dicInterno
    return dicNovoInv
        

#############################################################
dicMatdDiscNota= {'1612299': {'ENG1000': 7.8, 'FIS1033': 5.7, 'MAT1161': 7.6, 'QUI1740': 7.9}, 
                  '1413399': {'ENG1000': 8.4, 'MAT1161': 9.2, 'MAT1260': 5.3}, 
                  '1511188': {'FIS1033': 8.7, 'MAT1161': 8.5, 'QUI1740': 8.3}, 
                  '1412222': {'FIS1033': 6.8, 'MAT1161': 7.2, 'MAT1260': 5.9}, 
                  '1619999': {'ENG1000': 6.7, 'MAT1260': 5.1}, 
                  '1617777': {'MAT1260': 7.3, 'QUI1740': 9.4}, 
                  '1418833': {'ENG1000': 6.9, 'FIS1033': 6.1}, 
                  '1611155': {'MAT1260': 5.3, 'QUI1740': 8.9}, 
                  '1414466': {'FIS1033': 9.4, 'MAT1161': 5.5, 'MAT1260': 6.1}, 
                  '1312211': {'FIS1033': 6.7, 'QUI1740': 6.7}, 
                  '1713300': {'ENG1000': 8.3, 'FIS1033': 6.4, 'MAT1161': 5.4, 'MAT1260': 7.1}, 
                  '1111188': {'MAT1161': 4.5, 'MAT1260': 6.1}, 
                  '1412200': {'ENG1000': 6.2, 'MAT1260': 6.6}, 
                  '1519911': {'MAT1260': 9.1, 'QUI1740': 5.4}, 
                  '1512211': {'ENG1000': 8.3, 'MAT1161': 9.1}, 
                  '1417700': {'FIS1033': 8.6, 'QUI1740': 8.8}, 
                  '1618811': {'MAT1260': 4.8, 'QUI1740': 8.2}, 
                  '1511100': {'MAT1161': 7.1, 'MAT1260': 7.3}, 
                  '1414400': {'ENG1000': 8.2, 'MAT1161': 6.7, 'MAT1260': 6.7}}

print('\n-------- Teste do exercício 1 ------------')

exibeNotaNaDisc(dicMatdDiscNota,'1713300','FIS1033')
exibeNotaNaDisc(dicMatdDiscNota,'1312211','MAT1260')
exibeNotaNaDisc(dicMatdDiscNota,'2212211','MAT1260')


print('\n-------- Teste do exercício 2 ------------')
dAlunoseNotasDaDisc = criaDicAlNtDaDisc(dicMatdDiscNota)
print('\n DISCIPLINA com seus alunos e notas ')
for (disc,dAlNtDaDisc) in dAlunoseNotasDaDisc.items():
    print(disc,":", dAlNtDaDisc)
