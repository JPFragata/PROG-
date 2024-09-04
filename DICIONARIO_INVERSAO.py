# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 07:27:23 2024

@author: PC14
"""

# INVERSÃO DE DICIONÁRIOS

dProdsDoMerc= {
'Qbarato': {'biscoito': 4.3, 'leite': 3.2, 'suco': 7.1, 'chocolate': 6.4, 'detergente': 3.2, 'cerveja': 6.4, 'manteiga': 8.7}, 
'UltraK': {'biscoito': 3.5, 'leite': 3.3, 'suco': 8.9, 'chocolate': 6.9, 'detergente': 4.2, 'cerveja': 6.4, 'manteiga': 8.7}, 
'Market': {'biscoito': 4.5, 'leite': 3.2, 'suco': 7.5, 'chocolate': 6.6, 'detergente': 3.8, 'cerveja': 6.5, 'manteiga': 9.2}, 
'Preferis':{'biscoito': 4.65, 'leite': 3.4, 'suco': 8.1, 'chocolate': 8.1, 'detergente': 3.3, 'cerveja': 6.5, 'manteiga': 8.9}, 
'Escolhis': {'biscoito': 5.2, 'leite': 3.3, 'suco': 8.3, 'chocolate': 7.5, 'detergente': 3.9, 'cerveja': 6.4, 'manteiga': 8.6}
   }

#COMO CRIAR UM DICIONÁRIO INVERTIDO --> PRODUTO X MERCADO

dNovoInve = {}  #chave=produto valoor, valor=R$ nos mercados

for (mercado,dicInterno) in dProdsDoMerc.items():     #chave=mercado, valor=dicionário com chave=produto, valor=preco
    for (produto,preco) in dicInterno.items():
        dicInterno = dNovoInve.get(produto,{})
        dicInterno[mercado] = preco
        dNovoInve[produto] = dicInterno
    
print(dNovoInve)


      
            
        