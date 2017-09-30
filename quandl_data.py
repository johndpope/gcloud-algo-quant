import pandas as pd

import quandl
quandl.ApiConfig.api_key = 'nW629kYKyDBPBFq1fuHs'


# Companis of SP100 in 2010/9/30
SP100 = ['AA', 'AAPL', 'ABT', 'AEP', 'AMGN', 'AMZN', 'AVP', 'AXP',
        'BA', 'BAC', 'BAX', 'BHI', 'BK', 'BRK.B', 'BMY',
        'C', 'CAT', 'CL', 'CMCSA', 'COF', 'COP', 'COST', 'CPB', 'CSCO', 'CVS',
        'DD', 'DELL', 'DIS', 'DOW', 'DVN',
         'EMC', 'ETR', 'EXC', 'F', 'FCX', 'FDX', 'GD', 'GE', 'GILD', 'GOOG', 'GS',
        'HAL', 'HD', 'HNZ', 'HON', 'HPQ', 'IBM', 'INTC', 'JNJ', 'JPM', 'KFT', 'KO', 'LMT', 'LOW',
        'MA', 'MCD', 'MDT', 'MET', 'MMM', 'MO', 'MON', 'MRK', 'MS', 'MSFT',
        'NKE', 'NOV', 'NSC', 'NWSA', 'NYX',	'ORCL', 'OXY', 'PEP', 'PFE', 'PG', 'PM',
        'QCOM', 'RF', 'RTN', 'S', 'SLB', 'SLE', 'SO', 'T', 'TGT', 'TWX', 'TXN', 'UNH', 'UPS', 'USB', 'UTX',
        'VZ', 'WAG', 'WFC', 'WMB', 'WMT', 'WY', 'XOM', 'XRX']


data = quandl.get_table('WIKI/PRICES', ticker=SP100, date={'gte': '2000-01-01'}, paginate=True)
data.to_csv('data.csv')
print(data)