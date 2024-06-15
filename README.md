# oxr

`oxr` is a thin-wrapper over the [Open Exchange Rates API](https://openexchangerates.org/). It provides a type-safe interface to the API, allowing you to easily fetch exchange rates and convert between currencies.


## Installation

```bash
pip install oxr
```


## Usage

```python
import oxr

import datetime as dt

# Base default to USD
client = oxr.Client(app_id='your_app_id')

# Fetch the latest exchange rates
rates = client.latest(symbols=['EUR', 'JPY'])

# Convert 100 USD to EUR
converted = client.convert(amount, 'USD', 'EUR')

# Get time series data
timeseries = client.timeseries(start_date=dt.date(2020, 1, 1), end_date=dt.date(2020, 1, 31), symbols=['EUR', 'JPY'])

# Get open, high, low, close data
ohlc = client.ohlc(start_time=dt.datetime(2020, 1, 1), period="1m", symbols=['EUR', 'JPY'])
```

## License

MIT

