"""
    rudimentary, draft, experiemental, MUST BE REVISED/IMPROVED
    apply conditional formatting to an html table
"""
# import requests
import numpy as np
import pandas as pd
import time
# import yard

symbol_csv = pd.read_csv('csco.csv')

symbol_csv['symbol'] = 'CSCO'

symbol_csv.drop(columns=['Open', 'High', 'Low', 'Adj Close'], inplace=True)

symbol_csv['Date'] = pd.to_datetime(symbol_csv['Date'])

symbol_csv['Close'] = symbol_csv['Close'].round(decimals=2)

symbol = symbol_csv.query('Date > "1/1/2020"')

symbol['pdc'] = symbol['Close'].shift(1)

symbol['percent_change'] = (symbol[['Close', 'pdc']].pct_change(axis='columns')).pdc.round(decimals=2)

symbol = symbol[['symbol', 'Date', 'Close', 'percent_change']]

symbol.to_html('csco.html', index=False)

time.sleep(1)

with open('csco.html', 'r+') as webpage:
    page_source = webpage.read()

page_source_lines = page_source.splitlines()
page_source_lines[0]

lines_ = np.arange(0, len(page_source_lines), 1)
number_of_rows = page_source.count('<tr>')
number_of_columns = int(page_source.count('<td>') / number_of_rows)
columns_to_paint = [4] # STARTS AT 1 (not 0)

for column_to_paint in columns_to_paint:
    first_td = 7 + number_of_columns + column_to_paint - 1
    last_td = first_td + (number_of_rows - 1) * (number_of_columns + 2)
    all_td = np.arange(first_td, last_td + 1, (2 + column_to_paint + (number_of_columns - column_to_paint)))
    for td in all_td:
        # page_source_lines[td] = page_source_lines[td].replace('<td>', '<td style="color: #3CB371;">')
        # page_source_lines[td] = page_source_lines[td].replace('#3CB371;">-', '#FA8072;">-')
        page_source_lines[td] = page_source_lines[td].replace('<td>', '<td style="color: green;">')
        page_source_lines[td] = page_source_lines[td].replace('green;">-', 'red;">-')

new_html = str(page_source_lines)
new_html = new_html.replace("', '", '\n')
new_html = new_html.replace("['", '')
new_html = new_html.replace("']", '')

with open('csco.html', 'w') as f:
    f.seek(0) # rewind
    f.write(new_html)

time.sleep(1)
with open('csco.html', 'r+') as f:
    old = f.read()
    f.seek(0) # rewind
    f.write('''
<head>
<meta http-equiv="refresh" content="45">
<link href='https://fonts.googleapis.com/css?family=Roboto Mono' rel='stylesheet'>
</head>
<style>
.dataframe {
    font-size: 9pt;
    font-family: 'Roboto Mono';
    border-collapse: collapse;
    border: 1px solid silver;
}

.dataframe td, th {
    padding: 3px;
}

.dataframe td {
    text-align: right;
}

.dataframe th {
    text-align: center;
}
</style>\n
    ''' + old)

'''

if __name__ == '__main__':
    main()

'''
