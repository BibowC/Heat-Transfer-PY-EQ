# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 05:13:28 2023

@author: G1513
"""

import pandas as pd
import plotly.graph_objects as go


df1 = pd.read_excel('TESTEPAINEL1.xlsx')
df2 = pd.read_excel('TESTEPAINEL2.xlsx')


cols_to_plot = ['B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'Shroud', 'Ambiente']


fig1 = go.Figure()

for col in cols_to_plot:
    fig1.add_trace(go.Scatter(x=df1['Tempo(s)'], y=df1[col], name=col))

fig1.update_layout(title='Gráfico de Linhas - Teste 1',
                  xaxis_title='Tempo (s)',
                  yaxis_title='Temperatura')

fig1.write_html('plot1.html')


fig2 = go.Figure()

for col in cols_to_plot:
    fig2.add_trace(go.Scatter(x=df2['Tempo(s)'], y=df2[col], name=col))

fig2.update_layout(title='Gráfico de Linhas - Teste 2',
                  xaxis_title='Tempo (s)',
                  yaxis_title='Temperatura')

fig2.write_html('plot2.html')


fig1.show()
fig2.show()





