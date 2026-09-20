'''
Useful links:
https://dash-bootstrap-components.opensource.faculty.ai/
https://dash-bootstrap-components.opensource.faculty.ai/examples/
'''


import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd

app = dash.Dash(external_stylesheets=[dbc.themes.SPACELAB])

#Build table manually.
table_header = [
    html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name")]))
]

row1 = html.Tr([html.Td("Arthur"), html.Td("Dent")])
row2 = html.Tr([html.Td("Ford"), html.Td("Prefect")])
row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox")])
row4 = html.Tr([html.Td("Trillian"), html.Td("Astra")])

table_body = [html.Tbody([row1, row2, row3, row4])]

#Build table from data frame.
df = pd.DataFrame(
    {
        "First Name": ["Arthur", "Ford", "Zaphod", "Trillian"],
        "Last Name": ["Dent", "Prefect", "Beeblebrox", "Astra"],
    }
)

app.layout = dbc.Container([
    dbc.Alert("Hello Bootstrap! Success Alert", color="success"),
    dbc.Alert("Hello Bootstrap! Primary Alert", color="primary"),
    dbc.Table(table_header + table_body, bordered=True),
    dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, dark=True),
    dbc.Button("Secondary", color="secondary", className="mr-1")
], className="p-5")


if __name__ == "__main__":
    app.run_server(debug=True)
