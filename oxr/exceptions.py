from typing import ClassVar, Final


class Error(Exception):
    """Base exception class for `openexchangerates`."""

    code: ClassVar[int | None] = None


class InvalidCurrency(Error):
    """Raised when an invalid currency is provided."""

    code = 400


class InvalidDate(Error):
    """Raised when an invalid date is provided."""

    code = 400


class InvalidDateRange(Error):
    """Raised when an invalid date range is provided."""

    code = 400


class InvalidAppID(Error):
    """Raised when an invalid App ID is provided."""

    code = 401


from typing import Final
from openexchangerates.exceptions import (
    Error,
    InvalidAppID,
    InvalidCurrency,
    InvalidDate,
    InvalidDateRange,
)

_MAPPING: Final[dict[tuple[int, str], type[Error]]] = {
    (401, "invalid_app_id"): InvalidAppID,
    (400, "invalid_currency"): InvalidCurrency,
    (400, "invalid_date"): InvalidDate,
    (400, "invalid_date_range"): InvalidDateRange,
}


def get(code: int, message: str) -> type[Error] | None:
    """Get the error class for the given code and message."""
    return MAPPING.get((code, message), None)
