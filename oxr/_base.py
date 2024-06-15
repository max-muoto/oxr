from __future__ import annotations

import abc
import datetime as dt
from collections.abc import Awaitable
from typing import Final, Iterable

from oxr import responses
from oxr._types import Currency, Period

_BASE_URL: Final = "https://openexchangerates.org/api"


class BaseClient(abc.ABC):
    def __init__(
        self,
        app_id: str,
        *,
        base: Currency = "USD",
        base_url: str = _BASE_URL,
    ) -> None:
        self._app_id = app_id
        self._base = base
        self._base_url = base_url

    @abc.abstractmethod
    def latest(
        self,
        base: str | None = None,
        symbols: Iterable[Currency] | None = None,
        show_alternative: bool = False,
    ) -> responses.Rates | Awaitable[responses.Rates]: ...

    @abc.abstractmethod
    def historical(
        self,
        date: dt.date,
        base: str | None = None,
        symbols: Iterable[Currency] | None = None,
        show_alternative: bool = False,
    ) -> responses.Rates | Awaitable[responses.Rates]: ...

    @abc.abstractmethod
    def convert(
        self,
        amount: float,
        from_: str,
        to: str,
    ) -> responses.Conversion | Awaitable[responses.Conversion]: ...

    @abc.abstractmethod
    def time_series(
        self,
        start: dt.date,
        end: dt.date,
        symbols: Iterable[Currency] | None = None,
        base: str | None = None,
        show_alternative: bool = False,
    ) -> responses.TimeSeries | Awaitable[responses.TimeSeries]: ...

    @abc.abstractmethod
    def ohlc(
        self,
        start_time: dt.datetime,
        period: Period,
        base: str | None = None,
        symbols: Iterable[Currency] | None = None,
        show_alternative: bool = False,
    ) -> responses.OHLC | Awaitable[responses.OHLC]: ...
