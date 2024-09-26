# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:44:16 2024

@author: jpfragata
"""

from datetime import date
class Data:
    def __init__(self, dia=date.today().day,mes=date.today().month,ano=date.today().year):
        '''recebe um valor de dia, mes e ano, todos inteiros, e cria um objeto. 
           Default: : data atual
           Caso os valores fornecidos estejam incorretos, cria a data 1/1/1'''
        self.ano = ano
        self.mes = mes
        self.dia = dia
        if not self.isMesValido(mes) or not self.isDiaValido(dia):
            self.ano = 1
            self.mes = 1
            self.dia = 1
        self.djul=convDataDiaJuliano(self.dia,self.mes,self.ano)

 

    def __str__(self): 
        '''retorna uma string da data no format dd/mm/aaaa'''
        return "{:0>2d}/{:0>2d}/{:0>4d}".format(self.dia, self.mes,self.ano)
    
    def __repr__(self): 
        '''retorna uma string da data no format dd/mm/aaaa'''
        return "{:0>2d}/{:0>2d}/{:0>4d}".format(self.dia, self.mes,self.ano)

    def __sub__(self, outra): # dias entre duas datas
        '''recebe  uma  Data e retorna a quantidade de dias entre elas'''
        djnovo=abs(self.djul-outra.djul)+1
        return (djnovo)
    
    def __le__(self,outra):
        '''recebe  uma  Data e retorna True se for mais recente que a Data recebida  
            e False caso contrário.'''
        return(self.djul <=outra.djul)
    def __ge__(self,outra):
        '''recebe  uma  Data e retorna True se for mais antiga que a Data recebida  
            e False caso contrário.'''
        return(self.djul>= outra.djul)
    
    
    def diaDaSemana(self):
        '''Retorna o dia da semana'''
        tDia=('SABADO','DOMINGO','SEGUNDA','TERÇA','QUARTA','QUINTA','SEXTA')
        a = (12 - self.mes)// 10
        b = self.ano - a 
        c = self.mes + 12*a  
        d = b//100
        e=  d//4
        f = 2-d+e
        g = int(365.25*b)
        h=  int ( 30.6001 * (c + 1))
        i = f + g + h + self.dia + 5
        return(tDia[ i%7])
    
    
    def isBissexto(self):
        '''Retorna True se é ano bissexto ou False caso contrário'''
        ano=self.ano
        return ano%4==0 and (ano%100!=0 or ano%400==0)

    def isMesValido(self,mes):
        '''Retorna True se é um valor de mês válido ou False caso contrário'''
        return mes>0 and mes<13
    
    def isDiaValido(self,dia):
        '''Retorna True se é um dia válido para o mês ou False caso contrário'''
        tDias=(31,28,31,30,31,30,31,31,30,31,30,31)
        mes= self.mes
        if mes==2:
            if self.isBissexto():
                maior=29
            else:
                maior=28
        else:
            maior = tDias[mes-1]
        return dia>0 and dia<=maior
    #AUXILARES
def convDataDiaJuliano(dia,mes,ano):
    if mes < 3:
        ano=ano-1
        mes=mes+12
    A=int(ano/100)
    B=int(A/4)
    C=2-A+B
    D = int(365.25 * (ano + 4716))
    E = int(30.6001 * (mes + 1))
    F = D + E + dia + 0.5 + C - 1524.5
    return int(F)

def convDiaJulianoData(juliano):
    A = juliano
    if A > 2299160:
        B =int((A - 1867216.25) / 36524.25)
        C = A + 1 + B - int(B / 4)
    else:
        C = A
    D = C + 1524
    E = int((D - 122.1) / 365.25)
    F = int(E * 365.25)
    G = int((D - F) / 30.6001)
    H = D - F - int(G * 30.6001)
    if G < 14:
        I = G - 1
    else:
        I = G - 13
    if I > 2:
        J = E - 4716
    else:
        J = E - 4715
    if J > 0:
        K = J
    else:
        K = abs(J + 1)
    return(H,I,K)
