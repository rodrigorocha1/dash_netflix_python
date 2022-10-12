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

# =========  Layout  =========== #


layout = dbc.Card([

    dbc.Button(
        id='botao_acesso',
        href='/dashboard_total_acesso',
        color='write',
        title='btn_acesso',

        children=[
            html.Img(src='../assets/LogoMakr-50L4Xu.png',
                     className='perfil_name',
                     title='btn_acesso',
                     id='btn_acesso',
                     width='70px')
        ], style={
            'position': 'absolute',
            'width': '106px',
            'height': '83px',
            'left': '0px',
            'top': '354px'}
    ),
    dbc.Button(
        id='botao_tempo',
        href='/dashboard_tempo',
        color='write',
        title='btn_tempo',
        children=[
            html.Img(src='../assets/LogoMakr.png',
                     className='perfil_name',
                     sizes='',
                     width='70',
                     id='id_btn_tempo')
        ], style={'position': 'absolute',
                  'width': '100px',
                  'height': '100px',
                  'left': '0px',
                  'top': '548px',
                  'border-radius': '40px'}
    ),

], style={'box-sizing': 'border-box',
          'position': 'absolute',
          'width': '106px',
          'height': '1080px',
          'left': '0px',
          'top': '0px',
          'background': '#341A20',
          'border': '1px solid #CB2424',
          'border-radius': '40px'})
