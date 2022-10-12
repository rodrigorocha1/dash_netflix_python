import os
import dash
import json
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
from datetime import datetime, date

import pdb
from dash_bootstrap_templates import ThemeChangerAIO

# ===== Layout =====

cartao1 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4('Total de Acessos',
                        className='cart title',
                        id='id_total_acessos',
                        style={'position': 'absolute',
                               'width': '320px',
                               'height': '38px',
                               'left': '120px',
                               'top': '110px',
                               'font-family': 'Inter',
                               'font-style': 'normal',
                               'font-weight': '400px',
                               'font-size': '24px',
                               'line-height': '29px'
                               # 'color': '#FFFFFF'
                               })
            ]
        )

    ],
    style={'position': 'absolute',
           'width': '404px',
           'height': '153px',
           'left': '177px',
           'top': '24px',
           'background': '#341A20',
           'box-shadow': '0px 4px 4px rgba(0, 0, 0, 0.25)',
           'border-radius': '40px'}, id='id_cartao1'

)

cartao2 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4('Total de Horas Assistidas',
                        className='horas_assistidas_tittle',
                        id='id_total_horas',
                        style={'position': 'absolute',
                               'width': '320px',
                               'height': '38px',
                               'left': '50px',
                               'top': '110px',
                               'font-family': 'Inter',
                               'font-style': 'normal',
                               'font-weight': '400',
                               'font-size': '24px',
                               'line-height': '29px',
                               'text-align': 'center',
                               'color': '#FFFFFF'}
                        )
            ]
        )

    ],
    style={'position': 'absolute',
           'width': '404px',
           'height': '153px',
           'left': '600px',
           'top': '24px',
           'background': '#341A20',
           'box-shadow': '0px 4px 4px rgba(0, 0, 0, 0.25)',
           'border-radius': '40px'}

)

cartao3 = dbc.Card(
    [
        html.H4('Média de Horas assistidas',
                id='id_media_horas',
                style={'position': 'absolute',
                       'width': '320px',
                       'height': '38px',
                       'left': '50px',
                       'top': '110px',
                       'font-family': 'Inter',
                       'font-style': 'normal',
                       'font-weight': '400',
                       'font-size': '24px',
                       'line-height': '29px',
                       'text-align': 'center',
                       'color': '#FFFFFF'})

    ], style={'position': 'absolute',
              'width': '404px',
              'height': '153px',
              'left': '1023px',
              'top': '24px',
              'background': '#341A20',
              'box-shadow': '0px 4px 4px rgba(0, 0, 0, 0.25)',
              'border-radius': '40px'}
)

cartao4 = dbc.Card(
    [
        html.H4('Qtd de títulos assistidos',
                id='id_qtd_titulo',
                style={'position': 'absolute',
                       'width': '320px',
                       'height': '38px',
                       'left': '50px',
                       'top': '110px',
                       'font-family': 'Inter',
                       'font-style': 'normal',
                       'font-weight': '400',
                       'font-size': '24px',
                       'line-height': '29px',
                       'text-align': 'center',
                       'color': '#FFFFFF'})

    ], style={'position': 'absolute',
              'width': '404px',
              'height': '153px',
              'left': '1446px',
              'top': '24px',
              'background': '#341A20',
              'box-shadow': '0px 4px 4px rgba(0, 0, 0, 0.25)',
              'border-radius': '40px'}
)

cartoes = dbc.Row([
    dbc.Col(cartao1),
    dbc.Col(cartao2),
    dbc.Col(cartao3),
    dbc.Col(cartao4),

], id='id_conjunto_cartoes')
