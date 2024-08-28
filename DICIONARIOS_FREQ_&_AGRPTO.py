# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 07:27:45 2024

@author: PC14
"""

#-------------------------------- DICIONÁRIOS ---------------------------------

#   DICIONÁRIO DE FREQUENCIAS

dicFreq = {}
for (produto,tipo) in dicFreq.items():
    qtd = dicFreq.get(tipo,0)
    qtd += 1 
    dicFreq[tipo] = qtd
    
print(dicFreq)

# DICIONÁRIO DE AGRUPAMENTO

dicAgrupamento = {}
for (produto,tipo) in dicAgrupamento.items():
    lItens_Tipo = dicAgrupamento.get(tipo,[])
    lItens_Tipo.append(produto)
    dicAgrupamento[tipo] = lItens_Tipo
    
print(dicAgrupamento)

# ----------------------------------------------------------------------------

tProdTipo = ( 
        ('álcool Gel', 'higiene'),
        ('álcool90','limpeza'),
        ('água','bebida'),
        ('refrigerante','bebida'),
        ('chocolate','bebida'),
        ('desinfetante','limpeza'),
        ('sabonete','higiene'),
        ('cerveja','bebida'),
        ('água sanitária','limpeza'),
        ('biscoito','alimento'),
        ('café','matinal'),
        ('leite','matinal')
        )
tTipoDep = (
        ('higiene','z1'),
        ('limpeza','z1'),
        ('bebida','z2'),
        ('alimento','z3'),
        ('matinal','z3'),
         )

'''
1) Faça uma função que receba estas 
tabelas armazenadas em tuplas de 
tuplas  e 
retorne um dicionário produto:depósito
'''

dicProdutoTipo = dict(tProdTipo)
dicTipoDeposito = dict(tTipoDep)
dicProdDep = {}
for (produto,tipo) in dicProdutoTipo.items():
    deposito = dicTipoDeposito.get(tipo,'indeterminado')
    if deposito != 'indeterminado':
        dicProdDep[produto] = deposito

print(dicProdDep) 


'''
2)-->Dicionário de Frequências
Faça uma função que  receba  
o dicionário produtos x depósito  e
retorne um dicionário depósito: qt de produtos
'''

def retornaDicionarioDepositoQtd(dicProdDep):
        dicQtdProd = {}
        for (produto,deposito) in dicProdDep.items():
            qtd = dicQtdProd.get(deposito,0)
            qtd += 1 
            dicQtdProd[deposito] = qtd
        return dicQtdProd

'''
3)-->Dicionário de Agrupamentos
Faça uma função que  receba  
o dicionário produtos x depósito  e
retorne um dicionário depósito: lista de produtos
'''

def retornaDicionarioDepositoProd(dicProdDep):
    dicAgrup = {}
    for (produto,deposito) in dicProdDep.items():
        lItensDep = dicAgrup.get(deposito,[])
        lItensDep.append(produto)
        dicAgrup[deposito] = lItensDep
    return dicAgrup

'''
4)-->Dicionário de dicionários
Faça uma função que  receba  
o dicionário produto: tipo  e
o dicionário  tipo:depósito
retorne um dicionário de dicionários onde
dicionário externo tem
          como chave: o produto
                      valor: dicionário com
                                  chave: 'tipo' , valor: tipo do produto
                                  chave: 'dep' , valor: nome do depósito
'''
def retornaDicionarioDeDicionario(dicProdutoTipo,dicTipoDeposito):
    dicDeDic = {}
    for (produto,tipo) in dicProdutoTipo.items():
        deposito = dicProdDep.get(produto,'indeterminado')
        dicDeDic[produto] = {'tipo':tipo,'depósito':deposito}
    return dicDeDic


        