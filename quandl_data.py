import pandas as pd

import talib
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


def get_data_from_quandl(file='data.csv'):
    """Example function with PEP 484 type annotations.

    Args:
        param1: The first parameter.
        param2: The second parameter.

    Returns:
        The return value. True for success, False otherwise.

    """

    data = quandl.get_table('WIKI/PRICES', ticker=SP100, date={'gte': '2000-01-01'}, paginate=True)

    if file:
        data.to_csv(file)

    return data


def add_technical_indicators(data=None, csv_file='data.csv'):
    """Example function with PEP 484 type annotations.

    Args:
        data (pandas.DataFrame): DataFrame with option prices.
        param2: The second parameter.

    Returns:
        data (pandas.DataFrame) : DataFrame with data with technical indicators added

    """

    if csv_file:
        data = pd.read_csv(csv_file, index_col=0)

    if data is None:
        raise KeyError('You must provide data or csv_file')

    return data


if __name__ == "__main__":

    data = add_technical_indicators(csv_file='data.csv')
    data = data[data['ticker'] == 'AA']
    macd, macdsignal, macdhist = talib.MACD(data['close'].as_matrix(), fastperiod=12, slowperiod=26, signalperiod=9)
    print(macd)

