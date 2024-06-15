"""Test endpoints that don't require a paid plan."""

from __future__ import annotations

import datetime as dt
import os

import pytest

import oxr.asynchronous


@pytest.fixture
def client() -> oxr.asynchronous.Client:
    app_id = os.getenv("OXR_APP_ID")
    if not app_id:
        pytest.skip("OXR_APP_ID is not set")
    return oxr.asynchronous.Client(app_id)


@pytest.mark.asyncio
async def test_latest(client: oxr.asynchronous.Client) -> None:
    resp = await client.latest()
    assert resp["base"] == "USD"
    assert "EUR" in resp["rates"]
    assert "JPY" in resp["rates"]

    # Narrow the symbols.
    resp = await client.latest(symbols=["EUR"])
    assert resp["base"] == "USD"
    assert "EUR" in resp["rates"]
    assert len(resp["rates"]) == 1


@pytest.mark.asyncio
async def test_historical(client: oxr.asynchronous.Client) -> None:
    resp = await client.historical(dt.date(2021, 1, 1))
    assert resp["base"] == "USD"
    assert "EUR" in resp["rates"]
    assert "JPY" in resp["rates"]

    # Narrow the symbols.
    resp = await client.historical(dt.date(2021, 1, 1), symbols=["EUR"])
    assert resp["base"] == "USD"
    assert "EUR" in resp["rates"]
    assert len(resp["rates"]) == 1


@pytest.mark.asyncio
async def test_currencies(client: oxr.asynchronous.Client) -> None:
    resp = await client.currencies()
    assert "USD" in resp
    assert "EUR" in resp
    assert "JPY" in resp
    assert "ZAR" in resp


@pytest.mark.asyncio
async def test_usage(client: oxr.asynchronous.Client) -> None:
    resp = await client.usage()
    assert "status" in resp
    assert "plan" in resp["data"]
    assert "usage" in resp["data"]
    assert "daily_average" in resp["data"]["usage"]
