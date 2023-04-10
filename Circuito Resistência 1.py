# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 00:58:13 2023

@author: Carlos Eduardo Bibow Corrêa
"""

class CRT1:
    def __init__(self, Tinf1, Tinf2, Ts1, Ts2, q, R1, R2, R3, Rn) : #Variáveis para n Resistências

        self.Tinf1 = Tinf1
        self.Tinf2 = Tinf2
        self.Ts1 = Ts2
        self.Ts2 = Ts2
        self.q = q
        self.R1 = R1
        self.R2 = R2
        self.R3 = R3
        self.Rn = Rn
        
    def Calc(self):
        return ((self.Tinf1 - self.Tinf2)/(self.R1 + self.R2 + self.R3 + self.Rn))
        
#Dados problemas e Resistências Térmicas (ADicionar no init__)
Tinf1 = 100
Tinf2 = 2
q = 1370
A = 10
hr = 12
k = 1
L = 0.2
R1 = (1/(hr*A))
R2 = (L/(k*A))
R3 = 0
Rn = 0
Ts1 = 0
Ts2 = 0


Calc = CRT1(Tinf1, Tinf2, Ts1, Ts2, q, R1, R2, R3, Rn)

x = Calc.Calc()