#TODO: look here to see whether to use sub-plots https://plotly.com/python/subplots/

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import mysql.connector as sql

app = dash.Dash(external_stylesheets=[dbc.themes.SPACELAB])

db_connection = sql.connect(host='localhost', database='covid19', user='root', password='cacca1971')
ds = pd.read_sql('SELECT * FROM final_01', con=db_connection)
ds_countries = pd.read_sql('SELECT DISTINCT final_01_country FROM final_01 ORDER BY final_01_country', con=db_connection) #I will use the list of countries in one dropdown

controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Country 1"),
                dcc.Dropdown(
                    id="country_1",
                    options=[
                        {"label": col, "value": col} for col in ds_countries["final_01_country"]
                    ],
                    value="Select Country 1",
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Country 2"),
                dcc.Dropdown(
                    id="country_2",
                    options=[
                        {"label": col, "value": col} for col in ds_countries["final_01_country"]
                    ],
                    value="Select Country 2",
                ),
            ]
        ),
    ],
    body=True,
)

app.layout = dbc.Container(
    [
        html.H1("Compare Countries"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=2),
                dbc.Col(
                    [
                        dcc.Graph(id="graph_country_1"),
                        dcc.Graph(id="graph_country_2")],
                md=10)
            ],
            align="center"
        ),
    ],
    fluid=True,
)

@app.callback(
    Output("graph_country_1", "figure"),
    [
        Input("country_1", "value"),
    ],
)
def make_graph(country_1):
    ds_country_1 = ds[ds["final_01_country"] == country_1]

    data = [
        go.Bar(
            x = ds_country_1["final_01_date"],
            y = ds_country_1["current_positive"]
        )
    ]

    layout = {'xaxis_tickangle': -45}

    return go.Figure(data=data, layout=layout)


@app.callback(
    Output("graph_country_2", "figure"),
    [
        Input("country_2", "value"),
    ],
)
def make_graph(country_2):
    ds_country_2 = ds[ds["final_01_country"] == country_2]

    data = [
        go.Bar(
            x = ds_country_2["final_01_date"],
            y = ds_country_2["current_positive"]
        )
    ]

    layout = {'xaxis_tickangle': -45}

    return go.Figure(data=data, layout=layout)



if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
