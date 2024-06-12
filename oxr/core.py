from __future__ import annotations

from oxr import responses, exceptions, _exceptions
from typing import Any, Final, Iterable, Literal, TypeAlias, cast
import datetime as dt
import requests


_Endpoint: TypeAlias = Literal[
    "latest",
    "historical",
    "convert",
    "time-series",
    "ohlc",
    "usage",
]

_BASE_URL: Final = "https://openexchangerates.org/api"


class Client:
    """A client for the Open Exchange Rates API."""

    def __init__(
        self,
        app_id: str,
        *,
        base: responses.Currency = "USD",
        base_url: str = _BASE_URL,
    ) -> None:
        self.app_id = app_id
        self._base = base
        self._base_url = base_url

    def _get(
        self,
        endpoint: _Endpoint,
        params: dict[str, Any],
    ) -> dict[str, Any]:
        """Make a GET request to the API."""
        url = f"{self._base_url}/{endpoint}.json"
        response = requests.get(url, params={**params, "app_id": self.app_id})
        try:
            response.raise_for_status()
        except requests.HTTPError as error:
            msg = response.json().get("message", "")
            exc = _exceptions.get(response.status_code, msg)
            if exc is not None:
                raise exc from error
            raise exceptions.Error from error

        return response.json()

    def latest(
        self,
        base: str | None = None,
        symbols: Iterable[responses.Currency] | None = None,
        show_alternative: bool = False,
    ) -> responses.Rates:
        """Get the latest exchange rates.

        Args:
            base: The base currency.
            symbols: The target currencies.
            show_alternative: Whether to show alternative currencies.
                Such as black market and digital currency rates.
        """
        params = {"base": base or self._base, "show_alternative": show_alternative}
        if symbols is not None:
            params["symbols"] = ",".join(symbols)
        return cast(responses.Rates, self._get("latest", params))

    def historical(
        self,
        date: dt.date,
        base: str | None = None,
        symbols: Iterable[responses.Currency] | None = None,
        show_alternative: bool = False,
    ) -> responses.Rates:
        """Get historical exchange rates.

        Args:
            date: The date of the rates.
            base: The base currency.
            symbols: The target currencies.
            show_alternative: Whether to show alternative currencies.
                Such as black market and digital currency rates.
        """
        params = {
            "base": base or self._base,
            "date": date.isoformat(),
            "show_alternative": show_alternative,
        }

        if symbols is not None:
            params["symbols"] = ",".join(symbols)
        return cast(responses.Rates, self._get("historical", params))

    def convert(
        self,
        amount: float,
        from_: str,
        to: str,
    ) -> responses.Conversion:
        """Convert an amount between two currencies.

        Args:
            amount: The amount to convert.
            from_: The source currency.
            to: The target currency.
            date: The date of the rates to use.
        """
        params = {"from": from_, "to": to, "amount": amount}
        return cast(responses.Conversion, self._get("convert", params))

    def time_series(
        self,
        start: dt.date,
        end: dt.date,
        symbols: Iterable[responses.Currency] | None = None,
        base: str | None = None,
        show_alternative: bool = False,
    ) -> responses.TimeSeries:
        """Get historical exchange rates for a range of dates.

        Args:
            start: The start date of the range.
            end: The end date of the range.
            symbols: The target currencies.
            base: The base currency.
            show_alternative: Whether to show alternative currencies.
                Such as black market and digital currency rates.
        """
        params = {
            "start": start.isoformat(),
            "end": end.isoformat(),
            "show_alternative": show_alternative,
        }
        params["base"] = base or self._base
        if symbols is not None:
            params["symbols"] = ",".join(symbols)
        return cast(responses.TimeSeries, self._get("time-series", params))

    def olhc(
        self,
        start_time: dt.datetime,
        period: Literal["1m", "5m", "15m", "30m", "1h", "12", "1d", "1w", "1mo"],
        base: str | None = None,
        symbols: Iterable[responses.Currency] | None = None,
        show_alternative: bool = False,
    ) -> responses.OHLC:
        """Get the latest open, low, high, and close rates for a currency.

        Args:
            base: The base currency.
            symbols: The target currencies.
            show_alternative: Whether to show alternative currencies.
                Such as black market and digital currency rates.
        """
        params = {
            "start_time": start_time.isoformat(),
            "period": period,
            "show_alternative": show_alternative,
        }
        params["base"] = base or self._base
        if symbols is not None:
            params["symbols"] = ",".join(symbols)
        return cast(responses.OHLC, self._get("ohlc", params))

    def usage(self) -> dict[str, Any]:
        """Get the usage statistics for the API key."""
        return self._get("usage", {})
