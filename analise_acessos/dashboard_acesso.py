from dash import html, dcc
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc
import pandas as pd

# DataFrames


# ========== Layout ===================== #


layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(style={'position': 'absolute',
                               'width': '577px',
                               'height': '348px',
                               'left': '180px',
                               'top': '301px',
                               'background': '#341A20',
                               'border-radius': '40px'},

                        md=4, id='id_assistidas_ano'),
                dbc.Col(style={'position': 'absolute',
                               'width': '1146px',
                               'height': '348px',
                               'left': '800px',
                               'top': '301px',
                               'background': '#341A20',
                               'border-radius': '40px', }, md=4, id='id_assistidas_mes'),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    style={'position': 'absolute',
                           'width': '577px',
                           'height': '365px',
                           'left': '180px',
                           'top': '679px',
                           'background': '#341A20',
                           'border-radius': '40px'},
                    id='id_tabela_turno'
                ),
                dbc.Col(
                    style={'position': 'absolute',
                           'width': '577px',
                           'height': '365px',
                           'left': '800px',
                           'top': '679px',
                           'background': '#341A20',
                           'border-radius': '40px', }
                ),
                dbc.Col(
                    style={
                        'position': 'absolute',
                        'width': '549px',
                        'height': '365px',
                        'left': '1400px',
                        'top': '679px',
                        'background': '#341A20',
                        'border-radius': '40px',
                    }
                )
            ]
        )
    ]
)
