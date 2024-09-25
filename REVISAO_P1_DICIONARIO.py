# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Considere
# -->um dicionário chamado dLivros, onde as chaves são os nomes dos autores, 
# e os valores são dicionários internos que contêm as seguintes informações sobre 
# os autores e seus livros:

# nacionalidade: a nacionalidade do autor.
# data_nascimento: a data de nascimento do autor no formato dd/mm/aaaa.
# idioma: o idioma em que o autor escreveu seus livros.
# total_vendidos:o número total de livros vendidos pelo autor.
# títulos: uma lista com os títulos dos livros escritos pelo autor.

# Exemplo:
#  dLivros = {
#     "J.K. Rowling": {
#         "nacionalidade": "Britânica",
#         "data_nascimento": "31/07/1965",
#         "idioma": "Inglês",
#         "total_vendidos": 500000000,
#         "títulos": ["Harry Potter e a Pedra Filosofal", "Harry Potter e a Câmara Secreta"]
#     },
#     "Gabriel García Márquez": {
#         "nacionalidade": "Colombiana",
#         "data_nascimento": "06/03/1927",
#         "idioma": "Espanhol",
#         "total_vendidos": 50000000,
#         "títulos": ["Cem Anos de Solidão", "O Amor nos Tempos do Cólera"]
#     }}
   


# dNacionalidadeContinente = {
#     "Britânica": "Europa",
#     "Colombiana": "América do Sul",
#     "Brasileira": "América do Sul"}}


###################################################
# Questão 1.A:
#     Escreva uma função denominada ehDoSeculo19 que receba o dicionário interno de
#     de UM autor e retorna True se ele é nascido entre 1800 e 1899 ou  False, caso contrário
###################################################
#  Escreva a seguir a função mais_populoso

def ehDoSeculo19(dicInterno):
    data = dicInterno['data_nascimento']
    ano = int(data[6:])
    return ano >= 1800 and ano <= 1899
        

###################################################
# Questão 1.B:
#     Escreva uma função denominada quemDoSeculo19 que receba o dicionário dLivros
#     e retorna uma tupla com os autores que nasceram no século 19. Esta função deve ativar
#     a função do item 1.A

###################################################
#  Escreva a seguir a função quemDoSeculo19

def quemDoSeculo19(dLivros):
    l = []
    for (autor,dicInterno) in dLivros.items():
        if ehDoSeculo19(dicInterno):
            l.append(autor)
    return tuple(l)

###################################################
# Questão 1.C:
#     Escreva uma função denominada quantidadeDeLiveos que receba o dicionário dLivros
#     e retorna um dicionário onde a chave é o nome do autor e o valor é a quantidade 
#     média de exmplares vendidos ( total_vendidos /nº de livros inscritos )
###################################################
#  Escreva a seguir a função quantidadeDeLivros

def quantidadeDeLivros(dLivros):
    dic = {}
    for (autor,dicInterno) in dLivros.items():
        total_vendidos = dicInterno['total_vendidos']
        qtd_livros = 0
        for livro in dicInterno['títulos']:
            qtd_livros+=1 
        media = total_vendidos/qtd_livros
        dic[autor]=media
    return dic
    

###################################################   
# Questão 1.D:
#         Escreva uma função denominada quantidadeAutoresPorIdioma que receba 
#         o dicionário dLivros e retorna um dicionário onde a chave é o 
#         idioma e o valor é a quantidade de autores que escreveram no idioma
###################################################
#  Escreva a seguir a função quantidadeAutoresPorIdioma
 
def quantidadeAutoresPorIdiomas(dLivros):
    dic ={}
    for (autor,dicInterno) in dLivros.items():
        idioma = dicInterno['idioma']
        qtd_autor = dic.get(idioma,0)
        dic[idioma]= qtd_autor+1
    return dic

      
###################################################    
#  Questão 1.E:   
#     Escreva uma função, denominada mesmoContinente, que receba o 
#     dicionário dLivros,  o dicionario dNacionalidadeContinente e os nomes de 
#     dois autores, e, caso a nacionalidade dos autores seja do mesmo continente 
#     exiba na tela o nome dos autores e MESMO CONTINENTE ou o nome dos 
#     autores e respectivos continentes. Considere a possibilidade dos autores
#     não estarem no dicionário exibindo mensagens apropriadas.
#     Considere que se a nacionalidade de todos os autores está no dicionário 
#     dNacionalidadeContinente
###################################################
#  Escreva a seguir a função mesmoContinente
 
def mesmoContinente(dLivros,dNacionalidadeContinente,autor1,autor2):
    dicInt1 = dLivros.get(autor1)
    if dicInt1 == None:
        print('AUTOR NÃO EXISTENTE')
    dicInt2 = dLivros.get(autor2)
    if dicInt2 == None:
        print('AUTOR NÃO EXISTENTE')
    if dicInt1 and dicInt2:
        nac1 = dicInt1['nacionalidade']
        nac2 = dicInt2['nacionalidade']
        cont1 = dNacionalidadeContinente[nac1]
        cont2 = dNacionalidadeContinente[nac2]
        if cont1 == cont2:
            print(f'{autor1} e {autor2} são do mesmo continente: {cont1}')
        else:
            print(f'{autor1} é do continente {cont1} e {autor2} é do continente {cont2}')
            

###################################################   
# Questão 1.F:
#     Escreva a função denomeinada qtLivrosPorContinente que recebe o dicionário 
#     dLivros e o dicionario dNacionalidadeContinente e retorna um novo dicionário
#     onde a chave é o continente e o valor é o total de livros vendidos por todos 
#     os autores com nacionalidade neste continente
###################################################
#  Escreva a seguir a função qtLivrosPorContinente
 
def QtLivrosPorContinente(dLivros,dNacionalidadeContinente):
    dic={}
    for (autor,dicInterno) in dLivros.items():                  #PARA CADA AUTOR E SEU DICIONARIO INTERNO COM SUAS INFORMAÇÕES NO DICIONARIO DE LIVROS
        nacionalidade = dicInterno['nacionalidade']             #A NACIONALIDADE É O VALOR DA CHAVE 'NACIONALIDADE' NO DICIONARIO INTERNO
        continente = dNacionalidadeContinente[nacionalidade]    #O CONTINENTE É O VALOR DA CHAVE 'NACIONALIDADE' NO DICIONARIO DE CONTINENTES
        total_vendidos = dicInterno['total_vendidos']           #A QUANTIDADE DE LIVROS VENDIDAS PELO AUTOR É O VALOR DA CHAVE 'TOTAL DE VENDAS' NO DICIONÁRIO INTERNO
        qtd_livros = dic.get(continente,0)                      #PROCURA SE TEM A CHAVE CONTINENTE NO NOVO DICIONARIO VAZIO. COMO NÃO TEM, A QUANTIDADE ASSUME O VALOR 0 (ZER0)
        dic[continente]=qtd_livros+total_vendidos               #ADICIONA AO DICIONÁRIO VAZIO COMO CHAVE O CONTINENTE E COMO VALOR A QUANTIDADE INICIAL DE VENDAS (ZERO)...
    return dic                                                      #...ACRESCIDA DO VALOR DE VENDAS DO AUTOR DA VEZ.
        
       
###################################################        
# Questão 1.G:
#  Escreva a função denominada livrosPorContinente que recebe o dicionário 
#  dLivros e o dicionario dNacionalidadeContinente e retorna um novo dicionário
#  onde a chave é o continente e o valor é um dicionário com :
#      chave: autor
#      valor: lista de livros do autor
###################################################
#  Escreva a seguir a função livrosPorContinente

def LivrosPorContinente(dLivros,dNacionalidadeContinente):
    dic={}
    for (autor,dicInterno) in dLivros.items():
        nacionalidade = dicInterno['nacionalidade']
        continente = dNacionalidadeContinente[nacionalidade]
        livros = dicInterno['títulos']
        novoDicInt = dic.get(continente,{})
        novoDicInt[autor] = livros
        dic[continente] = novoDicInt
    return dic
        

###################################################
#  BP para teste de suas funções
###################################################

dLivros = {
    "J.K. Rowling": {
        "nacionalidade": "Britânica",
        "data_nascimento": "31/07/1965",
        "idioma": "Inglês",
        "total_vendidos": 500000000,
        "títulos": ["Harry Potter e a Pedra Filosofal", "Harry Potter e a Câmara Secreta"]
    },
    "Gabriel García Márquez": {
        "nacionalidade": "Colombiana",
        "data_nascimento": "06/03/1927",
        "idioma": "Espanhol",
        "total_vendidos": 50000000,
        "títulos": ["Cem Anos de Solidão", "O Amor nos Tempos do Cólera"]
    },
    "J.R.R. Tolkien": {
        "nacionalidade": "Britânica",
        "data_nascimento": "03/01/1892",
        "idioma": "Inglês",
        "total_vendidos": 300000000,
        "títulos": ["O Senhor dos Anéis", "O Hobbit"]
    },
    "Machado de Assis": {
        "nacionalidade": "Brasileira",
        "data_nascimento": "21/06/1839",
        "idioma": "Português",
        "total_vendidos": 10000000,
        "títulos": ["Dom Casmurro", "Memórias Póstumas de Brás Cubas"]
    },
    "Haruki Murakami": {
        "nacionalidade": "Japonesa",
        "data_nascimento": "12/01/1949",
        "idioma": "Japonês",
        "total_vendidos": 20000000,
        "títulos": ["Kafka à Beira-Mar", "Norwegian Wood"]
    },
    "George Orwell": {
        "nacionalidade": "Britânica",
        "data_nascimento": "25/06/1903",
        "idioma": "Inglês",
        "total_vendidos": 40000000,
        "títulos": ["1984", "A Revolução dos Bichos"]
    },
    "Stephen King": {
        "nacionalidade": "Americana",
        "data_nascimento": "21/09/1947",
        "idioma": "Inglês",
        "total_vendidos": 350000000,
        "títulos": ["O Iluminado", "It - A Coisa"]
    },
    "Isabel Allende": {
        "nacionalidade": "Chilena",
        "data_nascimento": "02/08/1942",
        "idioma": "Espanhol",
        "total_vendidos": 65000000,
        "títulos": ["A Casa dos Espíritos", "Paula"]
    },
    "Agatha Christie": {
        "nacionalidade": "Britânica",
        "data_nascimento": "15/09/1890",
        "idioma": "Inglês",
        "total_vendidos": 2000000000,
        "títulos": ["Assassinato no Expresso do Oriente", "O Caso dos Dez Negrinhos"]
    },
    "Ernest Hemingway": {
        "nacionalidade": "Americana",
        "data_nascimento": "21/07/1899",
        "idioma": "Inglês",
        "total_vendidos": 80000000,
        "títulos": ["O Velho e o Mar", "Por Quem os Sinos Dobram"]
    }
}
dNacionalidadeContinente = {
    "Britânica": "Europa",
    "Colombiana": "América do Sul",
    "Brasileira": "América do Sul",
    "Japonesa": "Ásia",
    "Americana": "América do Norte",
    "Chilena": "América do Sul",
    "Francesa": "Europa",
    "Alemã": "Europa",
    "Portuguesa": "Europa",
    "Italiana": "Europa",
    "Mexicana": "América do Norte",
    "Canadense": "América do Norte",
    "Indiana": "Ásia",
    "Chinesa": "Ásia",
    "Australiana": "Oceania",
    "Sul-Africana": "África",
    "Egípcia": "África",
    "Angolana": "África"
}

# # Teste da função ehDoSeculo19
print("Teste 1.A - ehDoSeculo19")

autor1 = dLivros["Machado de Assis"]  # Nasceu em 1839 (século 19)
autor2 = dLivros["J.K. Rowling"]  # Nasceu em 1965 (século 20)

print(ehDoSeculo19(autor1))  # Esperado: True
print(ehDoSeculo19(autor2))  # Esperado: False

# # Teste da função quemDoSeculo19
print("\nTeste 1.B - quemDoSeculo19")

autores_seculo19 = quemDoSeculo19(dLivros)
print(autores_seculo19)  # Esperado: ('Machado de Assis', 'Ernest Hemingway', 'Agatha Christie')

# # Teste da função quantidadeDeLivros
print("\nTeste 1.C - quantidadeDeLivros")

dmedia_vendas = quantidadeDeLivros(dLivros)
for (autor, media) in dmedia_vendas.items():
    print(f"{autor}: {media:.2f} livros vendidos em média")
    
# # Teste da função quantidadeAutoresPorIdiomas
print("\nTeste 1.D - quantidadeAutoresPorIdiomas")

dautores_por_idioma = quantidadeAutoresPorIdiomas(dLivros)
print(dautores_por_idioma)  # Esperado: {'Inglês': 6, 'Espanhol': 2, 'Português': 1, 'Japonês': 1}

# # Teste da função mesmoContinente
print("\nTeste 1.E - mesmoContinente")

mesmoContinente(dLivros, dNacionalidadeContinente, "J.K. Rowling", "Agatha Christie")  # Esperado: mesmo continente
mesmoContinente(dLivros, dNacionalidadeContinente, "Machado de Assis", "Gabriel García Márquez")  # Esperado: mesmo continente
mesmoContinente(dLivros, dNacionalidadeContinente, "J.K. Rowling", "Haruki Murakami")  # Esperado: continentes diferentes

# # Teste da função QtLivrosPorContinente
print("\nTeste 1.F - QtLivrosPorContinente")

dvendas_por_continente = QtLivrosPorContinente(dLivros, dNacionalidadeContinente)
print(dvendas_por_continente)
# # Esperado: {'Europa': 2840000000, 'América do Sul': 125000000, 'Ásia': 20000000, 'América do Norte': 430000000}

# # Teste da função LivrosPorContinente
print("\nTeste 1.G - LivrosPorContinente")

dlivros_por_continente = LivrosPorContinente(dLivros, dNacionalidadeContinente)
print(dlivros_por_continente)
# # Esperado: {'Europa': {'J.K. Rowling': ['Harry Potter e a Pedra Filosofal', 'Harry Potter e a Câmara Secreta'], 'J.R.R. Tolkien': ['O Senhor dos Anéis', 'O Hobbit'], 'George Orwell': ['1984', 'A Revolução dos Bichos'], 'Agatha Christie': ['Assassinato no Expresso do Oriente', 'O Caso dos Dez Negrinhos']}, 'América do Sul': {'Gabriel García Márquez': ['Cem Anos de Solidão', 'O Amor nos Tempos do Cólera'], 'Machado de Assis': ['Dom Casmurro', 'Memórias Póstumas de Brás Cubas'], 'Isabel Allende': ['A Casa dos Espíritos', 'Paula']}, 'Ásia': {'Haruki Murakami': ['Kafka à Beira-Mar', 'Norwegian Wood']}, 'América do Norte': {'Stephen King': ['O Iluminado', 'It - A Coisa'], 'Ernest Hemingway': ['O Velho e o Mar', 'Por Quem os Sinos Dobram']}}
