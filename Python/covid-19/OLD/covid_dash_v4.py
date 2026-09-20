#INFO: look here for information on sub-plots https://plotly.com/python/subplots/

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
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
                    value="US",
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Region 1"),
                dcc.Dropdown(
                    id="region_1",
                    value="",
                    placeholder="None",
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
                    value="Italy",
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Region 2"),
                dcc.Dropdown(
                    id="region_2",
                    value="",
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
                    ],
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
        Input("country_2", "value"),
        Input("region_1", "value"),
        Input("region_2", "value"),
    ],
)
def make_graph(country_1, country_2, region_1, region_2):
    measure_1 = "current_positive"
    measure_2 = "current_positive_delta"

    ds_country = ds.groupby(['final_01_country', 'final_01_date'])[[measure_1, measure_2]].sum().reset_index()
    ds_region = ds.groupby(['final_01_country', 'final_01_region' , 'final_01_date'])[[measure_1, measure_2]].sum().reset_index()

    if region_1 == "":
        ds_country_1 = ds_country[(ds_country['final_01_country'] == country_1)]
    else:
        ds_country_1 = ds_region[ds_region['final_01_region'] == region_1]

    if region_2 == "":
        ds_country_2 = ds_country[(ds_country['final_01_country'] == country_2)]
    else:
        ds_country_2 = ds_region[ds_region['final_01_region'] == region_2]

    def get_color(v):
        if v > 0:
            return 'red'
        else:
            return 'green'

    fig = make_subplots(
        rows=4, cols=1,
        subplot_titles=(country_1 + " - " + measure_1, country_1 + " - " +  measure_2, country_2  + " - " +  measure_1, country_2  + " - " +  measure_2),
        row_heights = [0.4, 0.2, 0.4, 0.2]
        )

    fig.add_trace(
        go.Bar(
            x = ds_country_1["final_01_date"],
            y = ds_country_1[measure_1],
            marker_color = '#1F77B4'
        ),
        row=1, col=1
    )

    colors = [get_color(v) for v in ds_country_1[measure_2]] #Picking color red if the increase is positive, otherwise green.

    fig.add_trace(
        go.Bar(
            x = ds_country_1["final_01_date"],
            y = ds_country_1[measure_1].pct_change(), #As I am aggregating values, I don't use the percent change in the db I have to calculate it here.
            marker_color = colors
        ),
        row=2, col=1
    )

    fig.add_trace(
        go.Bar(
            x = ds_country_2["final_01_date"],
            y = ds_country_2[measure_1],
            marker_color = '#bcbd22'
        ),
        row=3, col=1
    )

    colors = [get_color(v) for v in ds_country_2[measure_2]] #Picking color red if the increase is positive, otherwise green.

    fig.add_trace(
        go.Bar(
            x = ds_country_2["final_01_date"],
            y = ds_country_1[measure_1].pct_change(),
            marker_color = colors
        ),
        row=4, col=1
    )

    fig.update_layout(xaxis_tickangle=-45, showlegend=False, height=1200)

    return go.Figure(fig)


@app.callback(
    [
        Output("region_1", "options"),
        Output("region_2", "options")
    ],
    [
        Input("country_1", "value"),
        Input("country_2", "value")
    ]
)
def set_region_list(country_1, country_2):
    qry_1 = 'SELECT DISTINCT final_01_region FROM final_01 WHERE final_01_country = \'' + country_1 + '\' ORDER BY final_01_region'
    qry_2 = 'SELECT DISTINCT final_01_region FROM final_01 WHERE final_01_country = \'' + country_2 + '\' ORDER BY final_01_region'
    ds_regions_1 = pd.read_sql(qry_1, con=db_connection)
    ds_regions_2 = pd.read_sql(qry_2, con=db_connection)

    options_1 = [{"label": col, "value": col} for col in ds_regions_1["final_01_region"]]
    options_2 = [{"label": col, "value": col} for col in ds_regions_2["final_01_region"]]

    return options_1, options_2

if __name__ == "__main__":
    app.run_server(debug=True, port=8887)
