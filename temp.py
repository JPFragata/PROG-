# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def calculaLado(x1,y1,x2,y2):
    dist=((x1-x2)**2+(y1-y2)**2)**(1/2)
    return dist

def moldura():
    print('='*6)
    print('='*6)
    return

def perimetro(xA,yA,xB,yB,xC,yC):
    l1=calculaLado(xA, yA, xB, yB)
    l2=calculaLado(xB, yB, xC, yC)
    l3=calculaLado(xA, yA, xC, yC)
    perim=l1+l2+l3
    return perim



