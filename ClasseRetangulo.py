# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 06:59:59 2021

@author: Ferlin
"""

from ClassePonto import Ponto

class Retangulo():
    def __init__(self, pA=Ponto(0,0),pC=Ponto(1,1)):
        self.vie=pA
        self.vsd=pC
        self.vse=Ponto(pA.getX(),pC.getY())
        self.vid=Ponto(pC.getX(),pA.getY())
        
    def __str__(self):    
        return("Vértices IE:{}  ID:{} SE:{} SD:{}" .format(self.vie,self.vid,self.vse,self.vsd))
    def __repr__(self):    
        return("Vértices IE:{}  ID:{} SE:{} SD:{}" .format(self.vie,self.vid,self.vse,self.vsd))

    def base(self):
        return self.vie.disEntre2Pontos(self.vid)
    def altura(self):
        return self.vie.disEntre2Pontos(self.vse)
    def diagonal(self):
        return self.vie.disEntre2Pontos(self.vsd)
    def centro(self):
        return Ponto(self.vie.getX()+self.base()/2,self.vie.getY()+self.altura()/2)
    def area(self):
        return self.altura()*self.base()
        
    def __eq__(self,outro):
        return self.base()==outro.base() and self.altura() == outro.altura()
    def __lt__(self,outro):
        return self.base()<outro.base() or self.altura() < outro.altura()
