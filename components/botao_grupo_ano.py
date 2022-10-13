from dash import html, dcc
import dash_bootstrap_components as dbc

opcao_periodo = [{'label': 'Período completo', 'value': 0}]
periodo = [i for i in range(2018, 2023)]
for i, j in zip(periodo, periodo):
    opcao_periodo.append({'label': i, 'value': j})

botao_grupo = dbc.RadioItems(
    id="id_slider_ano",
    inline=True,
    labelCheckedClassName="active",
    options=opcao_periodo,
)

