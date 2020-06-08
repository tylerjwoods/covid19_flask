'''Instantiate a Dash app.'''
import numpy as numpy 
import pandas as pd
import dash 
import dash_table 
import dash_html_components as html 
import dash_core_components as dcc 
from .layout import html_layout

def create_dashboard(server):
    '''
    Create a Plotly Dash dashboard
    '''
    dash_app = dash.Dash(server=server,
                        routes_pathname_prefix='/dashapp/',
                        external_stylesheets=[
                            '/static/css/styles.css',
                            'https://fonts.googleapis.com/css?family=Lato'
                            ]
                        )

    # Prepare a DataFrame
    df = pd.read_csv('data/current_hospitals.csv')

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        children=[dcc.Graph(
            id='hospitalizations',
            figure={
                'data': [
                    {
                        'x': df.columns,
                        'y': df.loc['WA', :],
                        'name': 'Hospitalizations in WA',
                        'type': 'line'
                    }
                ],
                'layout': {
                    'title': 'Hospitalization in WA State',
                    'height': 500,
                    'padding': 150
                }
            }),
        ],
        id = 'dash-container'
    )
    return dash_app.server