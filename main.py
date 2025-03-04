# import currencyapicom

# client = currencyapicom.Client('cur_live_3FcuYOYZ7kwnGQsTWvI80gmfpxWel3qrP3op1jfs')
# eur = client.latest('EUR',currencies=['GBP','MUR','USD','ZAR'])
# gbp = client.latest('GBP',currencies=['EUR','GBP','MUR','USD','ZAR'])
# mur = client.latest('MUR',currencies=['EUR','GBP','USD','ZAR'])
# usd = client.latest('USD',currencies=['EUR','GBP','MUR','ZAR'])
# zar = client.latest('ZAR',currencies=['EUR','GBP','MUR','USD'])


# print(eur)
# print('+++++++++++++++++++++++++++++++++++++++++++++++')
# print(zar)

# # EUR
# # GBP
# # MUR
# # USD
# # ZAR

from dotenv import load_dotenv
import os

load_dotenv()  # This line brings all environment variables from .env into os.environ
print(os.environ['CURRENCY_API'])