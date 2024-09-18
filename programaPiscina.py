# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 16:26:56 2022

@author: Ferlin
"""

from ClasseRetangulo import *
from ClasseCirculo import *
from ClassePonto import *

terreno=Retangulo(Ponto(10,10), Ponto(40,30))
centro=terreno.centro()
piscina=Circulo(centro,terreno.altura()*0.3)
ilha=Circulo(centro,piscina.getRaio()*0.2)
areaIlha=ilha.area()
areaPiscina=piscina.area()-areaIlha
print("Área útil da piscina: {:.1f}m² - área da ilha: {:.1f}m²".format(areaPiscina,areaIlha))
