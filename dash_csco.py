"""
    learning DASH
    Luis Miguel - 2020-01-31
"""

# import yard
import dash
import dash_html_components as html
import dash_table
import pandas as pd

# yard.clear_screen()

symbol_csv = pd.read_csv('csco.csv')

symbol_csv['symbol'] = 'CSCO'

symbol_csv.drop(columns=['Open', 'High', 'Low', 'Adj Close'], inplace=True)

symbol_csv['Date'] = pd.to_datetime(symbol_csv['Date'])

symbol_csv['Close'] = symbol_csv['Close'].round(decimals=2)

symbol = symbol_csv.query('Date > "1/1/2020"')

symbol['pdc'] = symbol['Close'].shift(1)

symbol['percent_change'] = (symbol[['Close', 'pdc']].pct_change(axis='columns')).pdc.round(decimals=2)

symbol = symbol[['symbol', 'Date', 'Close', 'percent_change']]

app = dash.Dash(__name__)

app.layout = html.Div([
        html.Div([]),
        html.Div([
        dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in symbol.columns],
    data = symbol.to_dict('records'),
    # fixed_rows={ 'headers': True, 'data': 0 },
    style_cell={
        'height': 'auto',
        'minWidth': '20px',
        'width': '20px',
        'maxWidth': '20px',
        'whiteSpace': 'normal'
    },
    style_data_conditional=[
        {
            'if': {
                'column_id': 'symbol',
                # 'filter_query': '{volume} > 10000000'
            },
            'width': '20px',
        },
        {
            'if': {
                'column_id': 'percent_change',
                # 'filter_query': '{changePercent} eq "Montreal"'
                'filter_query': '{percent_change} > ' + str(0)
            },
            'backgroundColor': '#2E8B57', # sea green
            'color': 'white',
            'width': '40px',
        },
        {
            'if': {
                'column_id': 'percent_change',
                # 'filter_query': '{changePercent} eq "Montreal"'
                'filter_query': '{percent_change} < ' + str(0)
            },
            'backgroundColor': '#FF6347', # tomato
            'color': 'white',
            'width': '70px',
        },
    ]
)
        ]),
        html.Div([]),
        ]
        ,style={'display': 'grid', 'grid-template-columns': '30% 39% 30%', 'grid-gap': '1px',})


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=False)
