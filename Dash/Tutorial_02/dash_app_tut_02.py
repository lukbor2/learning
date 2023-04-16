# Tutorial is here:
# https://www.statworx.com/de/blog/how-to-build-a-dashboard-in-python-plotly-dash-step-by-step-tutorial/

import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# Load data
df = pd.read_csv('data/stockdata2.csv', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['Date'])

# Creates a list of dictionaries, which have the keys 'label' and 'value'.
def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list


#initialize the app
app = dash.Dash(__name__)

#define the app
app.layout = html.Div(children=[
                        html.Div(className='row',
                                 children=[
                                    html.Div(className='four columns div-user-controls',
                                             children=[
                                                html.H2('Dash - STOCK PRICES'),
                                                html.P('''Visualizing Time Series with Plotly and Dash'''),
                                                html.P('''Pick One or More Stock from the Dropdown Below'''),
                                                html.Div(className='div-for-dropdown',
                                                         children=[
                                                            dcc.Dropdown(id='stockselector',
                                                            options=get_options(df['stock'].unique()), #use the function get_options to build the list of options for the dropdown
                                                            multi=True,
                                                            value=[df['stock'].sort_values()[0]],
                                                            style={'backgroundColor': '#1E1E1E'},
                                                            className='stockselector')
                                                ], style={'color': '#1E1E1E'})

                                    ]), #define the left element
                                    html.Div(className='eight columns div-for-charts bg-grey',
                                             children=[
                                                dcc.Graph(id='timeseries', config={'displayModeBar': False}),
                                                dcc.Graph(id='change', config={'displayModeBar': False})

                                    ]) #define the right element
                                 ])

])

#Callback for time series price.
@app.callback(Output('timeseries', 'figure'),
              [Input('stockselector', 'value')])
def update_timeseries(selected_dropdown_value):
    #STEP 1
    trace = []
    df_sub = df

    # STEP 2
    # Draw and append traces for each stock.
    # go.Scatter is a plotly object that can be passed to figure to draw the data (i.e. trace) represented by that go.Scatter object.
    # In this example the data of each selected stock is used to build a go.Scatter object for that stock, then the list of go.Scatter object is used by figure to actuall draw the chart. This is how plotly works.

    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub[df_sub['stock'] == stock].index,
                                 y=df_sub[df_sub['stock'] == stock]['value'],
                                 mode='lines',
                                 opacity=0.7,
                                 name=stock,
                                 textposition='bottom center'))
    # STEP 3
    traces = [trace]
    data = [val for sublist in traces for val in sublist] #????

    # Define Figure
    # STEP 4
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Stock Prices', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
              ),

              }

    return figure

@app.callback(Output('change', 'figure'),
              [Input('stockselector','value')])
def update_change(selected_dropdown_value):
    trace = []
    df_sub = df
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub[df_sub['stock'] == stock].index,
                                y=df_sub[df_sub['stock'] == stock]['change'],
                                mode='lines',
                                name=stock,
                                opacity=0.7,
                                textposition='bottom center'))
    traces = [trace]
    data = [val for sublist in traces for val in sublist]

    figure = {'data': data,
              'layout': go.Layout(
               colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
               template='plotly_dark',
               paper_bgcolor='rgba(0, 0, 0, 0)',
               plot_bgcolor='rgba(0, 0, 0, 0)',
               margin={'t': 50},
               height=250,
               hovermode='x',
               autosize=True,
               title={'text': 'Daily Change', 'font': {'color': 'white'}, 'x': 0.5},
               xaxis={'showticklabels': False, 'range': [df_sub.index.min(), df_sub.index.max()]},
              ),
    }

    return figure

#run the app
if __name__ == '__main__':
    app.run_server(debug = True)
