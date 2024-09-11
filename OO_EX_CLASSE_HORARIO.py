# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 07:38:58 2024

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

# Utilizando a classe horário e a lista de ligações (hora de início e hora de término) realizadas por uma pessoa, mostre o tempo total
# que a pessoa gastou em ligações:
#  lLigacoes = [ ('08:00','08:10'),('09:50','10:10'),('10:15','11:00'),('12:00','13:00'),('13:50','14:15'),
#                ('16:00','17:00'),('17:00','18:15'),

# Cada elemento desta lista é uma tuplinha que representa:  horário do início da ligação e o horário de término da ligação


from classeUnidadeTempo import *
lLigacoes = [ ('08:00','08:10'),('09:50','10:10'),('10:15','11:00'),('12:00','13:00'),('13:50','14:15'),
               ('16:00','17:00'),('17:00','18:15')]

soma=Horario(0)
for (hI,hF) in lLigacoes:
    (h,m) = hI.split(':')           
    ObjetoHI = Horario(h=int(h),m=int(m))
    (h,m) = hF.split(':')
    ObjetoHF = Horario(h=int(h),m=int(m))
    # print(ObjetoHF-ObjetoHI)
    intervalo = ObjetoHF - ObjetoHI
    soma += intervalo
print(soma)

    
    
    
    
    






