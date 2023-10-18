import quandl as q

q.ApiConfig.api_key = "PdJ5XyKxE9o6iUeSsNgS"

q.ApiConfig.verify_ssl = False

print(data = q.get_table('ZACKS/FC', ticker='AAPL'))