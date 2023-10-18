import quandl as q

q.ApiConfig.api_key = ""

q.ApiConfig.verify_ssl = False

print(data = q.get_table('ZACKS/FC', ticker='AAPL'))