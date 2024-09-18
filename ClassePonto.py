# -*- coding: utf-8 -*-
"""
CLASSE PONTO:
Atributos: x,y
Métodos:
    Construtor (__init__):	 este método recebe os valores e cria um objeto . Default: pto  0,0
    Apresentação (__str__ e __repr__):	 retorna uma string com os valores dos atributos
    ptoMediano:	recebe  obj  pto e retorna um ponto com as coordenadas do ponto médio entre eles .
    alteraCoordenadas:	Recebe uma das coordenadas ou ambas e alterando as coordenadas deste ponto *
    getX:	Retorna o valor da coordenada x
    getY:	Retorna o valor da coordenada y
    distAOrigem:	Recebe a distância deste ponto até a origem
    disEntre2Pontos:	Recebe um Ponto e retorna  a distância entre elesade ou False , cc
    coefAngular:	Recebe um Ponto  e retorna o coeficiente angular entre os pontos
    clonar:	Constrói outro Ponto com os mesmos atributos 
    +:	Constrói novo ponto cujo x, y é a soma das coordenadas
    -:	Constrói um novo ponto  cujo x, y é a 
         diferença das coordenadas
    +=:	Soma às coordenadas do Ponto os valores da tupla (x,y) '
    ==:	Retorna True se os pontos têm mesmas coordenadas
    !=:	Retorna True se os pontos não têm mesmas coordenadas
    <:	Retorna True se  1º ponto está mais próximo da origem
    >:	Retorna True se  1º ponto está mais distante da origem

"""

class Ponto():
    # Construtor
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        return
    
    # Exibição via print e no interpretador
    def __str__(self):
         s= '({},{})'.format(self.getX(),self.getY())
         return s
    def __repr__(self):
         s= '({},{})'.format(self.getX(),self.getY())
         return s
    
    # Acesso aos atributos    
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    # Clonar 
    def clonar(self):
        c=Ponto(self.x,self.y)  # poderia ser self.getX(),self.getY()
        return c

    # Alteração dos Atributos
    def alteraCoordenada(self,eixo,valor):
        if eixo.upper()== 'X':
            self.x=valor
        else:
            self.y=valor
        return
    
    def alteraCoordenadas(self,valorX='',valorY=''):
        if valorX != '':
            self.x=valorX
        if valorY != '':
            self.y=valorY 
        return
    
    def setX(self,valor):
        self.x=valor
        return
    
    def setY(self,valor):
        self.y=valor
        return
    
    # Operadores Aritméticos definidos: + e -   
    def __add__(self,OutroPto):
        ''' construir um novo ponto 
        cujo x, y é a soma das coordenadas'''
        x=self.getX() + OutroPto.getX()
        y=self.getY() + OutroPto.getY()
        return Ponto(x,y)
    
    def __sub__(self,OutroPto):
        ''' construir um novo ponto 
        cujo x, y é a diferença das coordenadas'''
        x=self.getX() - OutroPto.getX()
        y=self.getY() - OutroPto.getY()
        return Ponto(x,y)
    
    def __iadd__(self,tupla):
        ''' Soma às coordenadas do Ponto os valores da tupla'''
        (deltax,deltay)=tupla
        self.x+=deltax
        self.y+=deltay
        return self
        
    
    # Operadores Relacionais definidos: ==, !=, < e > e -   
    def __eq__(self,OutroPto):
        return self.getX() == OutroPto.getX() and \
                self.getY() == OutroPto.getY()
                
    def __neq__(self,OutroPto):
        return self.getX() != OutroPto.getX() or  \
                self.getY() != OutroPto.getY()
                
    def __lt__(self,OutroPto):
        d1= self.distAOrigem()
        d2= OutroPto.distAOrigem()
        return d1<d2
    
    def __gt__(self,OutroPto):
        d1= self.distAOrigem()
        d2= OutroPto.distAOrigem()
        return d1>d2
    
    # Outros métodos
    def distAOrigem(self):
        d= (self.getX()**2 + self.getY()**2)**0.5
        return d   
    
    def disEntre2Pontos(self,OutroPto):
        d= ((self.getX()-OutroPto.getX())**2 + (self.getY()- OutroPto.getY())**2)**0.5
        return d
    
    def ptoMediano(self,OutroPto):
        x=(self.getX()+OutroPto.getX())/2
        y=(self.getY()+OutroPto.getY())/2
        return Ponto(x,y)
    
    def coefAngular(self,outro): 
        x1=self.getX()  #poderia ser também  x1=self.x
        x2=outro.getX()
        y1=self.getX()
        y2=outro.getY()
        m=(y2-y1)/(x2-x1)
        return abs(m)
     
    






