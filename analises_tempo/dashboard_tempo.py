import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(style={'position': 'absolute',
                               'width': '577px',
                               'height': '348px',
                               'left': '135px',
                               'top': '301px',
                               'background': '#341A20',
                               'border-radius': '40px'},
                        id='id_horas_assistidas_ano'
                        ),
                dbc.Col(style={
                    'position': 'absolute',
                    'width': '1146px',
                    'height': '348px',
                    'left': '732px',
                    'top': '301px',

                    'background': '#341A20',
                    'border-radius': '40px'}, id='id_horas_assistidas_mes')
            ]
        ),
        dbc.Row(
            [
                dbc.Col(style={'position': 'absolute',
                               'width': '745px',
                               'height': '365px',
                               'left': '135px',
                               'top': '679px',
                               'background': '#341A20',
                               'border-radius': '40px', }
                        , id='id_comparacao_horas_turno'),
                dbc.Col(style={'position': 'absolute',
                               'width': '981px',
                               'height': '365px',
                               'left': '897px',
                               'top': '679px',
                               'background': '#341A20',
                               'border-radius': '40px', }, id='id_total_hora_serie_semana')
            ]
        )
    ]
)
