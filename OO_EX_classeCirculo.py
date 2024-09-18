# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 08:00:50 2024

@author: PC14
"""


from ClassePonto import Ponto
import math

class Circulo:

    def __init__(self,c=Ponto(0,0),r=1):
        self.centro = c
        self.raio = r
        
    def __str__(self):
        # Monta uma string ==> centro:(x,y) -  raio: r
        return (f'Centro: {self.centro} - Raio: {self.raio}')
        
        
    def __repr__(self):
        # Monta a representação interna ==>  c:(x,y) -  r: r]
        return (f'Centro: {self.centro} - Raio: {self.raio}')
    
    def __eq__(self,outro):
        ''' recebe outro circulo e retorna True se mesmos atributos, False cc'''
        return self.centro == outro.centro and self.raio == outro.raio
           
    def __neq__(self,outro):
       ''' recebe outro circulo e retorna True se atributos distintos, False cc'''
       return self.centro != outro.centro or self.raio != outro.raio
        
    def __lt__(self,outro):
        ''' recebe outro circulo e retorna True, se menor raio'''
        return self.raio < outro.raio
            
    def  __gt__(self,outro):
        ''' recebe outro circulo e retorna True, se maior raio'''
        return self.raio > outro.raio
     
    def __add__(self,outro):
        ''' recebe  como parâmetro um outro objeto da classe Círculo e 
        retorna um novo Círculo cujo centro é o ponto mediano entre os círculos 
                                  e o raio é a soma dos raios  '''
        raio = self.raio + outro.raio
        (x1,y1) = (self.centro.getX(),self.centro.getY())
        (x2,y2) = (outro.centro.getX(),outro.centro.getY())
        (x,y) = ((x1+x2)/2,(y1+y2)/2)
        return (f'Centro: {(x,y)} - Raio: {raio}')
    
    
    def __sub__(self,outro):
        ''' recebe  como parâmetro um outro objeto da classe Círculo e 
        retorna um novo Círculo cujo centro é o ponto mediano entre os círculos
                                            e o raio é a subtração dos raios  '''
        raio = self.raio + outro.raio
        (x1,y1) = (self.centro.getX(),self.centro.getY())
        (x2,y2) = (outro.centro.getX(),outro.centro.getY())
        (x,y) = ((x1+x2)/2,(y1+y2)/2)
        return (f'Centro: {(x,y)} - Raio: {raio}')
    
    def __mul__(self,v):
        ''' recebe  como parâmetro um número e 
        retorna um novo círculo com mesmo centro e raio multiplicado pelo valor'''
        raio = self.raio*v
        return (f'Centro: {self.centro} - Raio: {raio}')
    
    def __truediv__(self,v):
        ''' recebe  como parâmetro um número e 
        retorna um novo círculo com mesmo centro e raio dividido pelo valor'''
        raio = self.raio/v
        return (f'Centro: {self.centro} - Raio: {raio}')        
    
    def __iadd__(self,valorRaio):
        ''' soma ao raio o valor recebido'''
        self.raio += valorRaio
        return self.raio
    
    # def __isub__(self,t):
    #     ''' diminui as coordenadas do centro considerando (x,y) recebido'''
    #     self.centro = 
        
    def getCentro(self):
        ''' retorna o ponto do centro'''
        return self.centro

    def getRaio(self):
        ''' retorna o valor do raio '''
        return self.raio
    
    def setCentro(self,pto):
        ''' recebe um pto que  torna-se o centro do circulo '''
        self.centro = Ponto(pto)   

    def setRaio(self,val):
        ''' recebe um valor que  torna-se o raio do círculo '''
        self.raio = val
    
    def area(self):
        ''' retorna a área do círculo'''
        return math.pi*self.raio**2
        
    def perimetro(self):
        ''' retorna o perímetro do círcunferência'''
        return 2*math.pi*self.raio

    # def clonar(self):
    #     ''' cria um novo circulo com mesmas coordenadas de centro e mesmo raio'''
        
        
    def interior(self,pto):
        ''' True se ponto está dentro do círculo, False, cc '''
        
        
        