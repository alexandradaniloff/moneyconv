import requests
import json
from config import keys

class Convertionexception(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base:str, amound: str ):
        if quote == base:
            raise Convertionexception('Введите разные валюты.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise Convertionexception(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise Convertionexception(f'Не удалось обработать валюту {base}.')

        try:
            amound = float(amound)
        except ValueError:
            raise Convertionexception(f'Не удалось обработать количество переводимой валюты {amound}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base