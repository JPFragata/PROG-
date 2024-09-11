# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 08:13:02 2024

@author: PC14
"""

# Considere a classe Horario ( disponível no arquivo classeHorarioSimplificada.py):
# Horario - Representa uma unidade de tempo
# •	Atributos:  h, m, s 
# •	Métodos:
# •	construtor:        este método constrói um objeto Horario, com os seguintes defaults: h=0, m=0, s=0.  

# •	apresentação: retorna uma string com os valores dos atributos no formato "hh:mm:ss"

# •	-:	 recebe um outro Horario e retorna um novo Horario  equivalente a diferença de tempo entre os horários recebidos
# •	+:	 recebe um outro Horario e retorna um novo Horario  equivalente a soma dos tempos dos horários recebidos
# •	+=:	recebe um outro Horario e atualiza o Horário com a soma dos tempos dos horários recebidos

# •	==: recebe como parâmetro um outro objeto da classe Horário, realizando a operação de comparação equivalente ao operador relacional
# •	!=:	
# •	>:
# •	<:	

# •	totSegundos: retorna o tempo em s
# •	totMinutos: retorna o tempo em minutos
# •	totHoras: retorna o tempo em horas

# •	getSeg:	retorna os segundos do horário
# •	getMin:	retorna os minutos do horário
# •	getHora:	retorna as horas do horário


# •	setSeg:	recebe um valor e altera o atributo minuto. pode recalcular o valor da hora e do minuto, quando segundos >60
# •	setMin:	recebe um valor e altera o atributo minuto. pode recalcular o valor da hora, quando mintos >60
# •	setHora: recebe um valor e altera o atributo hora. Recalcula o tempo decorrido
    
    	
# •	clone:	o objeto clona a si próprio, para isto, ele cria um novo objeto da classe Horario com os mesmos valores de atributos e retorna sua referência 

# Utilizando a classe horário e o registro de ponto dos estagiários armazenado na lista abaixo:
  # lPontos = [ (20,1,'10:00','11:10'),(20,1,'16:50','18:00'),
  #           (30,1,'10:00','15:00'),
  #           (40,1,'15:00','18:00'),
            
            
  #           (20,2,'10:00','18:00'),
  #           (30,2,'10:00','15:00'),
  #           (40,2,'08:00','12:10'),
 
  #           (20,3,'16:00','17:00'),
  #           (30,3,'10:00','15:00'),
  #           (40,3,'15:00','20:00'),

  #           (20,5,'12:00','15:00'),
  #           (30,5,'08:00','10:00'),(30,5,'12:00','18:00')]
# Cada elemento desta lista representa:  código do estagiário, dia, horário de entrada e horário de saída
# Construa um dicionário cuja chave é código do estagiário e o valor é o tempo total trabalhado pelo estagiário no formato ( h: m:s).
# Exiba o dicionário construído.

from classeUnidadeTempo import *
lPontos = [ (20,1,'10:00','11:10'),(20,1,'16:50','18:00'),
            (30,1,'10:00','15:00'),
            (40,1,'15:00','18:00'),
            
            
            (20,2,'10:00','18:00'),
            (30,2,'10:00','15:00'),
            (40,2,'08:00','12:10'),
 
            (20,3,'16:00','17:00'),
            (30,3,'10:00','15:00'),
            (40,3,'15:00','20:00'),

            (20,5,'12:00','15:00'),
            (30,5,'08:00','10:00'),(30,5,'12:00','18:00')]

dic = {}
for (codigo,dia,hE,hS) in lPontos:
    (h,m) = hE.split(':')
    ObjetoHI = Horario(h=int(h),m=int(m))
    (h,m) = hS.split(':')
    ObjetoHS = Horario(h=int(h),m=int(m))
    tempo = ObjetoHS - ObjetoHI                     #ACHADO O INTERVALO DE TEMPO
    tempo_atual = dic.get(codigo,Horario(0))        #SE O TEMPO NÃO EXISTIR NO DICIONÁRIO, ADICIONA TEMPO 00:00:00
    dic[codigo] = tempo_atual + tempo               #ADICIONA O CÓDIGO COMO CHAVE E SUBSTITUI O HORARIO ANTERIOIR PELO ANTERIOR SOMADO AO NOVO
print(dic)
    