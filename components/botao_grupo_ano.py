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

botao_grupo = dcc.Slider(id='id_slider_ano',
                         step=None,
                         marks={i: str(i) for i in [2016, 2017, 2018, 2019, 2020, 2021, 2022]},
                         )
