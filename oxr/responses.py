from typing import Literal, TypeAlias, TypedDict


# fmt: off
Currency: TypeAlias =  Literal[
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD",
    "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP",
    "BYN", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP", "CNH", "CNY", "COP", "CRC", "CUC",
    "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD",
    "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL",
    "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD",
    "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK",
    "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP",
    "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR",
    "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD",
    "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD",
    "SSP", "STD", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY",
    "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VES", "VND", "VUV",
    "WST", "XAF", "XAG", "XAU", "XCD", "XDR", "XOF", "XPD", "XPF", "XPT", "YER", "ZAR",
    "ZMW", "ZWL"
]
# fmt: on


class _Base(TypedDict):
    """The base response from the API."""

    disclaimer: str
    license: str


class Rates:
    """The response for the latest and historical endpoints."""

    timestamp: int
    base: Currency
    rates: dict[Currency, float]


# Functional typed dict to use 'from' as a key.
_ConversionRequest = TypedDict(
    "_ConversionRequest",
    {"query": str, "from": Currency, "to": Currency, "amount": float},
)


class _ConversionMeta(TypedDict):
    timestamp: int
    rate: float


class Conversion(_Base):
    """The response for the convert endpoint."""

    query: _ConversionRequest
    meta: _ConversionMeta
    response: float


class TimeSeries:
    """The response for the time series endpoint."""

    start_date: str
    end_date: str
    base: Currency
    rates: dict[str, dict[Currency, float]]


class _OHLCRates(TypedDict):
    open: float
    high: float
    low: float
    close: float
    average: float


class OHLC(_Base):
    """The response for the olhc endpoint."""

    start_time: str
    end_time: str
    base: Currency
    rates: dict[Currency, _OHLCRates]
