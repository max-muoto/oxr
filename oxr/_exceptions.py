from typing import Final
from openexchangerates.exceptions import (
    Error,
    InvalidAppID,
    InvalidCurrency,
    InvalidDate,
    InvalidDateRange,
)

_EXCEPTION_MAP: Final[dict[tuple[int, str], type[Error]]] = {
    (401, "invalid_app_id"): InvalidAppID,
    (400, "invalid_currency"): InvalidCurrency,
    (400, "invalid_date"): InvalidDate,
    (400, "invalid_date_range"): InvalidDateRange,
}


def get(code: int, message: str) -> type[Error] | None:
    """Get the error class for the given code and message."""
    return _EXCEPTION_MAP.get((code, message), None)
