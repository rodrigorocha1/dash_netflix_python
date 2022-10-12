from dash import html, dcc
import dash_bootstrap_components as dbc

opcao_periodo = [{'label': 'período completo', 'value': 0}]
periodo = [i for i in range(2018, 2023)]
for i, j in zip(periodo, periodo):
    opcao_periodo.append({'label': i, 'value': j})

botao_grupo = dbc.RadioItems(
    id="id_slider_ano",
    className="btn-group",
    inputClassName="btn-check",
    labelClassName="btn btn-outline-primary",
    labelCheckedClassName="active",
    options=opcao_periodo,
)

