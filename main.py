import currencyapicom
from dotenv import load_dotenv
import os

# Load all environment variables from .env 
load_dotenv()

# currencies = {}

# client = currencyapicom.Client(os.environ['CURRENCY_API'])
# currencies['eur'] = client.latest('EUR',currencies=['GBP','MUR','USD','ZAR'])
# currencies['gbp'] = client.latest('GBP',currencies=['EUR','GBP','MUR','USD','ZAR'])
# currencies['mur'] = client.latest('MUR',currencies=['EUR','GBP','USD','ZAR'])
# currencies['usd'] = client.latest('USD',currencies=['EUR','GBP','MUR','ZAR'])
# currencies['zar'] = client.latest('ZAR',currencies=['EUR','GBP','MUR','USD'])

# print(currencies)




jason = {'eur': {'meta': {'last_updated_at': '2025-03-03T23:59:59Z'}, 'data': {'GBP': {'code': 'GBP', 'value': 0.8254537584}, 'MUR': {'code': 'MUR', 'value': 48.6313845297}, 'USD': {'code': 'USD', 'value': 1.0485146702}, 'ZAR': {'code': 'ZAR', 'value': 19.4908428347}}}, 'gbp': {'meta': {'last_updated_at': '2025-03-03T23:59:59Z'}, 'data': {'EUR': {'code': 'EUR', 'value': 1.2114548995}, 'GBP': {'code': 'GBP', 'value': 1}, 'MUR': {'code': 'MUR', 'value': 58.914729059}, 'USD': {'code': 'USD', 'value': 1.2702282344}, 'ZAR': {'code': 'ZAR', 'value': 23.6122770478}}}, 'mur': {'meta': {'last_updated_at': '2025-03-03T23:59:59Z'}, 'data': {'EUR': {'code': 'EUR', 'value': 0.0205628528}, 'GBP': {'code': 'GBP', 'value': 0.0169736841}, 'USD': {'code': 'USD', 'value': 0.0215604528}, 'ZAR': {'code': 'ZAR', 'value': 0.4007873315}}}, 'usd': {'meta': {'last_updated_at': '2025-03-03T23:59:59Z'}, 'data': {'EUR': {'code': 'EUR', 'value': 0.9537300988}, 'GBP': {'code': 'GBP', 'value': 0.7872600946}, 'MUR': {'code': 'MUR', 'value': 46.3812151723}, 'ZAR': {'code': 'ZAR', 'value': 18.5890034624}}}, 'zar': {'meta': {'last_updated_at': '2025-03-03T23:59:59Z'}, 'data': {'EUR': {'code': 'EUR', 'value': 0.0513061446}, 'GBP': {'code': 'GBP', 'value': 0.0423508499}, 'MUR': {'code': 'MUR', 'value': 2.4950888447}, 'USD': {'code': 'USD', 'value': 0.0537952452}}}}

for x in jason:
    date = jason[x]['meta']['last_updated_at'][:10]
    print(f'{x} | {date} = {jason[x]}')

# date
# print()




















# EUR
# GBP
# MUR
# USD
# ZAR