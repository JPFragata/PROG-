# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 08:22:48 2024

@author: PC14
"""

#LISTA DE FIXAÇÃO DE TUPLAS


# 2A --------------------------------
def recebeString(s):
    maior=s[0]
    cont=0
    for letra in s:
        if letra>maior:
            maior=letra
            cont=1
        elif letra==maior
            cont+=1
    return (maior,cont)

(maior,cont)=recebeString('baboseirasssss')
print(f'Maior 

# 2B --------------------------------

def minmax(lista):
    maior=lista[0]
    menor=lista[0]
    contMaior=0
    contMenor=0
    for item in lista:
        if item>maior:
            maior=item        
        if item<menor:
            menor=item
    for item in lista:
        if item == maior:
            contMaior+=1 
        if item == menor:
            contMenor+=1 
    return ((menor,contMenor),(maior,contMaior))

lista=[1,3,2,5.3,1,78,5,8,6,8,5]

# 3 ----------------------------------

def reajuste(minimo,maximo,preco,taxa):
    if preco>=minimo and preco<=maximo:
        reajuste=preco*(taxa+1)
        return (preco,reajuste)
    else:
        return(preco)

t=reajuste(10,20,10,1)
if len(t)==2:
    print(f'Preco = {t[0]}, Reajuste = {t[1]})
else:
    print(f'Preco = {t[0]})

# 4 ----------------------------------

# 4A
'''
# ERRADO
def exibeContas(tupla_contas):
    for conta in tupla_contas:
        for item in conta:
            print(item)
 '''   
#CERTO

def exibeContas(tupla_contas):
    for (descricao,valor,dtPgto) in tupla_contas
        print(f'conta: {descricao}, valor: {valor}, data de pagamento: {dtPgto})
        
# 4B

def valorMedioContas(tuplas_contas):
    valor_total=0
    qtd_contas=0
    for conta in tuplas_contas:
        valor=conta[1]
        valor_total+=valor
        qtd_contas+=1
    valor_medio=round(valor/qtd_contas,2)
    return valor_medio

# 4C

def exibeContasMaisCarasQueValorMedio(tupla_contas):
    valor_medio=valorMedioContas(tupla_contas)
    print(f'Valor médio: R${valor_medio}')
    for (tipo,valor) in tupla_contas:
        if valor>valor_medio:
            print(f'Deve pagar a conta de {tipo}')
            
# 4D      

def contasMaisCarasQueValorMedio(tupla_contas):
    valor_medio=valorMedioContas(tupla_contas)
    lcontas=[]
    for conta in tupla_contas:
        valor=conta[1]
        if valor>valor_medio:
            lcontas.append(conta)
    return (valor_medio,tuple(lcontas))

# 4E

def contasDaData(tupla_contas,data):
    for conta in tupla_contas:
        tipo=conta[0]
        vencimento=conta[2]
        if vencimento==data:
            print(f'Pagar a conta de {tipo} em {vencimento}')
            
# 4F -------------------- PROBLEMA -------------------------------

def exibeDescrValor(tupla_contas,mes_inicial,mes_final):
    lcontas=[]
    for conta in tupla_contas:
        tipo=conta[0]
        vencimento=conta[2]
        mes=vencimento[3:5]
        if mes in range(mes_inicial,mes_final+1):
            lcontas.append(tipo)
    return tuple(lcontas)
            
contas = (('LUZ',250.95,'8/9'),('ÀGUA',340,'25/11'),('GÁS',110.65,'30/10'))
          


    
