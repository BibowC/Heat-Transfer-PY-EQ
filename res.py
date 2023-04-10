# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 02:15:45 2023

@author: G1513
"""

import sympy as sp

# Define as variáveis simbólicas
Tinf1, Tinf2, hr, A, L, K, Q = sp.symbols('Tinf1 Tinf2 hr A L K Q')

# Define a equação
Q_expr = (Tinf1 - Tinf2) / ((1/(hr*A)) + (L/(K*A)))

# Inverte a equação para hr
hr_expr = sp.solve(Q_expr - Q, hr)
a_expr = sp.solve(Q_expr - Q, A)

# Define os valores dos parâmetros
Tinf1_value = 100
Tinf2_value = 50
#A_value = 10
L_value = 5
K_value = 2
Q_value = 100
hr_value = 0.4

# Substitui os valores dos parâmetros na equação invertida para obter o valor de hr
#hr_value = hr_expr[0].subs({Tinf1: Tinf1_value, Tinf2: Tinf2_value, A: A_value, L: L_value, K: K_value, Q: Q_value})
A_value = a_expr[0].subs({Tinf1: Tinf1_value, Tinf2: Tinf2_value, L: L_value, K: K_value, hr: hr_value, Q: Q_value})
#Q_value = (Tinf1_value - Tinf2_value) / ((1/(hr_value*A_value)) + (L_value/(K_value*A_value)))


# Imprime o valor de hr
print(f"O valor de hr é {A_value}")