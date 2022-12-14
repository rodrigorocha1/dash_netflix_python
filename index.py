from dash import html, dcc
from dash.dependencies import Input, Output, State
from app import *

from analises_tempo.dashboard_tempo import layout as layout_tempo
from analise_acessos.dashboard_acesso import layout as layout_acesso
from components import barra_lateral, cartoes, botao_grupo_ano

# =========  Layout  =========== #

app.layout = html.Div(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            barra_lateral.layout
        ], md=2),
        dbc.Col([
            dcc.Location(id='cartoes'),
            cartoes.cartoes

        ]),
        dbc.Col([
            html.Div([
                botao_grupo_ano.botao_grupo,

            ], style={'position': 'absolute',
                      'width': '953px',
                      'height': '98px',
                      'left': '483px',
                      'top': '25px',
                      'border-radius': '0px'}),

            html.Div(id='id_out_slider',
                     style={'position': 'absolute', 'top': '70px', 'margin-top': '15px', 'left': '269px'})

        ], style={'position': 'absolute',
                  'width': '1469px',
                  'height': '78px',
                  'left': '269px',
                  'top': '192px',
                  'border': '1px solid #CB2424',
                  'border-radius': '40px'}),

        dbc.Col([
            html.Div(id="page-content")
        ]),
    ])
], style={"padding": "0px"})


@app.callback(
    Output('id_out_slider', 'children'),
    Input('id_slider_ano', 'value')
)
def output(value):
    return f'Selecionou: {value} Tipo {type(value)} '


@app.callback(Output("page-content", "children"),
              [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/dashboard_tempo":
        return layout_tempo
    else:
        return layout_acesso


if __name__ == "__main__":
    app.run_server(port=8051, debug=True)
