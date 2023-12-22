from datetime import datetime, timezone, timedelta
import requests
import os
from .models import *


def get_values_from_polygon_api(
        date_from: str,
        date_to: str,
        stocks_ticker: str = 'AAPL',
        multiplier: str = '1',
        timespan: str = 'day'
) -> list:
    params = {'adjusted': 'true', 'sort': 'asc', 'limit': '500'}
    url = f'https://api.polygon.io/v2/aggs/ticker/{stocks_ticker}/range/{multiplier}/{timespan}/{date_from}/{date_to}'
    headers = {'Authorization': f'Bearer {os.getenv("POLYGON_API_KEY")}'}
    response = requests.get(url, headers=headers, params=params)
    data = response.json() if response.status_code == 200 else None
    resp = []
    if data:
        for item in data['results']:
            item['t'] = datetime.fromtimestamp(item['t'] / 1000.0, tz=timezone.utc)
            resp.append(item)
    return resp


def get_values(
        date_from: str,
        date_to: str,
        stocks_ticker: str = 'AAPL',
        multiplier: str = '1',
        timespan: str = 'day'
) -> list:
    date_from_dt = list(map(int, date_from.split('-')))
    date_from_dt = datetime(date_from_dt[0], date_from_dt[1], date_from_dt[2])
    date_to_dt = list(map(int, date_to.split('-')))
    date_to_dt = datetime(date_to_dt[0], date_to_dt[1], date_to_dt[2])
    resp = list(StockPrice.objects.filter(
        timestamp__gte=date_from_dt, timestamp__lte=date_to_dt+timedelta(days=1), ticker=stocks_ticker
    ).order_by('timestamp'))
    try:
        timestamps_from_api = get_values_from_polygon_api(date_from, date_to, stocks_ticker, multiplier, timespan)
        timestamps = set(item.timestamp for item in resp)
        result = [item for item in timestamps_from_api if item['t'] not in timestamps]
        new_objects = StockPrice.objects.bulk_create([
            StockPrice(
                ticker=stocks_ticker,
                volume=item['v'],
                volume_weighted=item['vw'],
                open_price=item['o'],
                close_price=item['c'],
                high_price=item['h'],
                low_price=item['l'],
                timestamp=item['t'],
                trades_count=item['n']
            ) for item in result
        ])
        resp.extend(new_objects)
        return resp
    except:
        return resp
