import quandl
quandl.ApiConfig.api_key = 'nW629kYKyDBPBFq1fuHs'

data = quandl.get_table('WIKI/PRICES', ticker=['A', 'AAPL'], paginate=True)
print(data)