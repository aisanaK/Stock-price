# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import plotly.graph_objects as go
import yfinance as yf
from dash import Dash, dcc, html

app = Dash(__name__)


tsla = yf.Ticker('TSLA')
tsla_data = tsla.history(period='1y')
print(tsla_data.head())
fig = go.Figure(data=go.Scatter(x=tsla_data.index, y=tsla_data["Close"]))

app.layout = html.Div(
    children=[
        html.H1(children='Hello Dash'),
        html.P(
            children='''
        Dash: A web application framework for your data.
    '''
        ),
        dcc.Graph(id='example-graph', figure=fig),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
