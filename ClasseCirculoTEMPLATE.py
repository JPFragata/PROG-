

from ClassePonto import Ponto
import math

class Circulo:

    def __init__(self,c=Ponto(0,0),r=1):
        

    def __str__(self):
        # Monta uma string ==> centro:(x,y) -  raio: r
        
    def __repr__(self):
        # Monta a representação interna ==>  c:(x,y) -  r: r]
        
    
    def __eq__(self,outro):
        ''' recebe outro circulo e retorna True se mesmos atributos, False cc'''
       
    def __neq__(self,outro):
       ''' recebe outro circulo e retorna True se atributos distintos, False cc'''
      
    def __lt__(self,outro):
        ''' recebe outro circulo e retorna True, se menor raio'''
        
    def  __gt__(self,outro):
        ''' recebe outro circulo e retorna True, se maior raio'''
        
     
    def __add__(self,outro):
        ''' recebe  como parâmetro um outro objeto da classe Círculo e 
        retorna um novo Círculo cujo centro é o ponto mediano entre os círculos 
                                  e o raio é a soma dos raios  '''
    
    def __sub__(self,outro):
        ''' recebe  como parâmetro um outro objeto da classe Círculo e 
        retorna um novo Círculo cujo centro é o ponto mediano entre os círculos
                                            e o raio é a subtração dos raios  '''
    
    def __mul__(self,v):
        ''' recebe  como parâmetro um número e 
        retorna um novo círculo com mesmo centro e raio multiplicado pelo valor'''
    
    
    def __truediv__(self,v):
        ''' recebe  como parâmetro um número e 
        retorna um novo círculo com mesmo centro e raio dividido pelo valor'''
    
    
    def __iadd__(self,valorRaio):
        ''' soma ao raio o valor recebido'''
    
    def __isub__(self,t):
        ''' diminui as coordenadas do centro considerando (x,y) recebido'''
       
    def getCentro(self):
        ''' retorna o ponto do centro'''

    def getRaio(self):
        ''' retorna o valor do raio '''
    
    
    def setCentro(self,pto):
        ''' recebe um pto que  torna-se o centro do circulo '''
    
    

    def setRaio(self,val):
        ''' recebe um valor que  torna-se o raio do círculo '''
       
    
    def area(self):
        ''' retorna a área do círculo'''
        
    def perimetro(self):
        ''' retorna o perímetro do círcunferência'''
        

    def clonar(self):
        ''' cria um novo circulo com mesmas coordenadas de centro e mesmo raio'''
        
    def interior(self,pto):
        ''' True se ponto está dentro do círculo, False, cc '''
       
    
   