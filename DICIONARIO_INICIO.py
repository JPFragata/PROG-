# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
A) Crie o dicionário de patinhos onde a chave é o nome e o valor a lista com alt, massa
    exiba-o
B) Sobre o dicionário de Patinhos:
  -->Recuperando valor de uma chave (acessando um item)
    a) Mostre os dados do Donald
    b) Mostre os dados de um patinho cujo nome é fornecido pelo usuário
        Se não existir??? --> exibir mensagem fulano não consta no dicionário
        Se não existir --> perguntar os dados e incluí-lo
        
  --> Inserindo/Alterando um item    
    c) Inclua o Peninha com 1.20m e 60 kg    
    d) Altere a altura do Donald para 1.30
    e) Obtenha o nome, altura e massa de um patinho via teclado
       Se o patinho já existe--> atualizar dados
       Se o patinho não existe --> incluir
       
  --> Visões e Percurso
    f) Mostre o nome dos patinhos no dicionário  
    g)	Acrescente ao peso dos 3 primeiros patinhos (considerando a ordem alfabética do nome), 10% do peso médio
        Dica: Classificar as chaves por nome
    h) Construa uma tupla com a altura e o peso médio dos patinhos (acessar só os valores)   
    i)	Iterando sobre o dicionário: Mostre o nome e o IMC (peso/altura2) de cada um
        •	Modificação: Construa um novo dicionário cuja chave é o nome e o valor é o IMC
        
  --> Atualizando vários elementos de um dicionário com update
    j)	Atualize o dicionário  dPat com o seguinte dicionário:
        d2= {'Clarabela': [2.20,78],'Margarida':[1.10,40]  }
        
  --> Eliminando um item
    k) Retire o Peninha exibindo seus dados

'''
def calcIMC(alt,massa):
    return massa/(alt**2)

def obtemPatinho():
    nome=input("Nome?")
    alt=float(input("Altura de %s?"%nome))
    peso=float(input("Peso de %s?"%nome))
    return (nome, [alt,peso])


tPatinhos =  (('Huguinho',[1.20,45]),
              ('Luisinho',[1.10,60]),
              ('Zezinho',[1.00,100]),
              ('Patinhas',[1.10,40 ]),
              ('Clarabela', [2.3, 80]),
              ('Donald',[1.20,50]))

#A) Crie o dicionário de patinhos onde a chave é o nome e o valor a lista com alt, massa
#   exiba-o


dicPatinhos=dict(tPatinhos)

print('\n##############################################\n')
print('A) dPatinhos criado')
print(dicPatinhos)
print('\n##############################################\n')

# B) Sobre o dicionário de Patinhos:
#   -->Recuperando valor de uma chave (acessando um item)
#     a) Mostre os dados do Donald
#     b) Mostre os dados de um patinho cujo nome é fornecido pelo usuário
#         Se não existir??? --> exibir mensagem fulano não consta no dicionário
#         Se não existir --> perguntar os dados e incluí-lo e exibir o dicionário

#a
print("B.a): mostre os dados do Donald")

print(dicPatinhos['Donald'])

#b
print("B.b: mostre os dados do patinho perguntado ao usuario")         

nome=input('Patinho? ') 
print(dicPatinhos[nome])
  
print("2b.1: Dados ou mensagem")

print(dicPatinhos.get('Donald'))
print(dicPatinhos.get('Marcelo'))
print(dicPatinhos.get('Marcelo','não existe'))


print("2b.2: Dados ou inclusão")
      
print('\ndPatinhos possivelmente atualizado')

print('\n##############################################\n')  
   
#   --> Inserindo/Alterando um item (exibir o dicionário após operação)
#     c) Inclua o Peninha com 1.20m e 60 kg    
#     d) Altere a altura do Donald para 1.30
#     e) Obtenha o nome, altura e massa de um patinho via teclado
#        Se o patinho já existe--> atualizar dados
#        Se o patinho não existe --> incluir

#LETRA C
dicPatinhos['Peninha']=[1.20,60]
print(dicPatinhos)

#LETRA D
dicPatinhos['Donald'][0]=1.30
print(dicPatinhos)

#LETRA E
(chave,valor)=obtemPatinho()
if chave not in dicPatinhos:
    dicPatinhos[chave]=valor









print('\n##############################################\n')  
#c
print('\n##############################################\n')
print("B.c): Inclusão do Peninha")

print('\n##############################################\n')  
#d
print('\n##############################################\n')
print("B.d): Alteração do Donald")

print('\n##############################################\n')  


#e
print('\n##############################################\n')
print("B.e): Obtem dados e inclui ou altera")
print("B.e.1): Teste de inclusão")
      
print('\n-------------------------------------------------\n')
      
print("B.e.2): Teste de alteração")
print('\n##############################################\n')  




#   --> Visões e Percurso
#     f) Mostre o nome dos patinhos no dicionário  
#     g)	Acrescente ao peso dos 3 primeiros patinhos 
#          (considerando a ordem alfabética do nome), 10% do seu peso
#         Dica: Classificar as chaves por nome
#     h) Construa uma tupla com a altura e o peso médio dos patinhos (acessar só os valores)   
#     i)	Iterando sobre o dicionário: Mostre o nome e o IMC (peso/altura2)
#      de cada um
#         •	Modificação: Construa um novo dicionário cuja chave é o nome e o valor é o IMC

print('Visões e Percursos')

#f ----------------------------------------
print('B.f- Nome dos patinhos:')

print(dicPatinhos.keys()) # MOSTRA AS CHAVES
print(dicPatinhos.values())     #MOSTRA OS VALORES
print(dicPatinhos.items())      #MOSTRA OS PARES DE CHAVES E VALORES

#g ---------------------------------------
print('B.g- Atualização do peso dos 3 primeiros considerando a ordem alfabética:')

print('\nB.g- dPatinhos alterado')

print('\n-------------------------------------------------\n')
#h
print('B.h- Tupla com altura e peso médio dos patinhos:')


print('\n-------------------------------------------------\n')
print('B.i.1- Nome e IMC e de cada patinho:')

print('\n-------------------------------------------------\n')
print('B.i.2- Dicionário com chave=Nome e  Valor = IMC dos patinhos:')



print('\n##############################################\n')  

       
#   --> Atualizando vários elementos de um dicionário com update
#     j)	Atualize o dicionário  dPat com o seguinte dicionário:
#         d2= {'Clarabela': [2.20,78],'Margarida':[1.10,40]  }

print('\n##############################################\n') 
print('B.j) Atualizando dicionário via update')


# --> Eliminando um item
# k) Retire o Peninha exibindo seus dados
#
print('\n##############################################\n')
print("B.k): Dados do Peninha e dicionário atualizado")