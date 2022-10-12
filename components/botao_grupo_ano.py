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

# options=[{"label": f'{i}', "value": f'{i}', "disabled": False} for i in range(2018, 2023)],

# botao_grupo = dcc.Checklist(
#     [i for i in range(2018, 2023)],
#     id='id_slider_ano',  style={'display':'block'}
# )


# botao_grupo = dcc.Slider(id='id_slider_ano',
#                          step=None,
#                          marks={i: str(i) for i in [2016, 2017, 2018, 2019, 2020, 2021, 2022]},
#                          value=2016
#                          )
