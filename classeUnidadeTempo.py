# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:09:11 2020

@author: cf
"""
from datetime import datetime
'''
Horario - Representa uma unidade de tempo
    Atributos:  h, m, s 
Métodos:
    construtor:
        este método constrói um objeto Horario, com os seguintes defaults: 
            h=0, m=0, s=0.  
        
    apresentação:	 
        retorna uma string com os valores dos atributos no formato "hh:mm:ss"
        
    -:	 recebe um outro Horario e retorna um novo Horario  equivalente a diferença de tempo entre os horários recebidos
    +:	 recebe um outro Horario e retorna um novo Horario  equivalente a soma dos tempos dos horários recebidos
    +=:	recebe um outro Horario e atualiza o Horário com a soma dos tempos dos horários recebidos
    	
    ==: Recebe  como parâmetro um outro objeto da classe Horário, realizando a operação de comparação equivalente ao operador relacional
    !=:	
    >:
    <:	
    	
    getSeg:	retorna os segundos do horário
    getMin:	retorna os minutos do horário
    getHora:	retorna as horas do horário
    	
    setSeg:	recebe um valor  e  altera o atributo segundo. pode recalcular o valor da hora e do minuto, quando segundos >60
    setMin:	recebe um valor  e  altera o atributo minuto. pode recalcular o valor da hora, quando mintos >60
    setHora: recebe um valor  e  altera o atributo hora. Recalcula o tempo decorrido
    
    	
    clone:	o objeto clona a si próprio, para isto, ele cria um novo objeto da classe Horario com os
    	mesmos valores de atributos e retorna sua referência 
    
    totSegundos: retorna o tempo em s
    totMinutos: retorna o tempo em minutos
    totHoras: retorna o tempo em horas
 
'''
class Horario:
    def __init__(self, h=0,m=0,s=0):
        tot = h*3600+m*60 + s
        (self.hora,self.min,self.seg)=transforma(tot)
        self.tempo = tot
        return
    
    def __str__(self):
        '''Monta uma string hh:mm:ss de exibição usada pelo print'''
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(self.hora, self.min,self.seg)
    def __repr__(self): 
        '''Monta uma string hh:mm:ss de exibição usada para representação interna usada pelo interpretador '''
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(self.hora, self.min,self.seg)
    
    def __add__(self,outro):
        ''' retorna um novo Horario com a soma dos tempos dos operandos'''       
        tot=abs(self.tempo+outro.tempo)
        return geraHorario(tot)
    def __sub__(self,outro):
        ''' retorna um novo Horario com a subtração dos tempos dos operandos'''       
        dif=abs(self.tempo-outro.tempo)
        return geraHorario(dif)
    
    def __iadd__(self,outro):
        '''atualiza o Horario, somando o tempo do outro'''
        tot=abs(self.tempo+outro.tempo)
        self.setTempo(tot)
        (self.hora,self.min,self.seg)=transforma(tot)
        return self
    
    def __eq__(self,outro):
        return(self.tempo==outro.tempo)
    def __ne__(self,outro):
        return(self.tempo != outro.tempo)
    def __lt__(self,outro):
        return(self.tempo<outro.tempo)
    def __gt__(self,outro):
        return(self.tempo>outro.tempo)

    def setSeg(self,s):
        '''recebe um valor  e  altera o atributo segundo. pode recalcular o valor da hora e do minuto, quando segundos >60'''
       
        tot=self.tempo-self.seg+s
        (self.hora,self.min,self.seg)=transforma(tot)
        self.tempo = tot
       
    def setMin(self,m):
        '''recebe um valor  e  altera o atributo minuto. pode recalcular o valor da hora, quando mintos >60'''
        
        tot=self.tempo-60*self.min+60*m
        (self.hora,self.min,self.seg)=transforma(tot)
        self.tempo = tot
        
    def setHora(self,h):
            '''recebe um valor  e  altera o atributo hora. Recalcula o tempo decorrido'''
     
            tot=self.tempo-3600*self.hora+3600*h
            (self.hora,self.min,self.seg)=transforma(tot)
            self.tempo = tot
     
    def setTempo(self,tot):
            self.tempo = tot
            (self.h,self.m,self.s)=transforma(tot)
    

    def getSeg(self):
        '''retorna os segundos do horário'''
        return self.seg
    def getMin(self):
        '''retorna os minutos do horário'''
        return self.min
    def getHora(self):
        '''retorna as horas do horário'''
        return self.hora
    
    def totSegundos(self):
        '''retorna o tempo em s'''
        return self.tempo
    def totMinutos(self):
        '''retorna o tempo em minutos'''
        return self.tempo/60
    def totHoras(self):
        '''retorna o tempo em horas'''
        return self.tempo/3600

    def copia(self):
        '''cria um novo objeto Horario com os dados do original'''
        return Horario(self.hora,self.min,self.seg,self.tempo)
    
##### funções auxiliares #######

def transforma(tempo):
    h=tempo//3600
    m=tempo%3600//60
    s=tempo%3600%60
    return (h,m,s)

def geraHorario(tempo):
    (h,m,s)=transforma(tempo)
    return Horario(h,m,s)
