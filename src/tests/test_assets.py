import pytest
from src.data.assets import create_asset, get_asset_by_symbol, list_assets, delete_asset

def test_create_assets():
    assert delete_asset("AAPL") is True #If you run the test for a second, you have to clean this up, otherwise you'll get an error
    assert create_asset("AAPL", "Apple Inc.", "stock", "NASDAQ", "USD") is True
    row = get_asset_by_symbol("AAPL")
    assert row["name"] == "Apple Inc."
    assert row["exchange"] == "NASDAQ"

def test_list_assets():
    create_asset("MSFT", "Microsoft Corp", "stock", "NASDAQ", "USD")
    create_asset("BTC-USD", "Bitcoin", "crypto", "Coinbase", "USD")
    assets = list_assets()
    symbols = {a["symbol"] for a in assets}
    assert {"MSFT", "BTC-USD"} <= symbols

    
def test_delete_asset():
    create_asset("TSLA", "Tesla Inc.", "stock", "NASDAQ", "USD")
    assert delete_asset("TSLA") is True
    assert get_asset_by_symbol("TSLA") is None
    
#To make sure the connection works and you don't get an error w/local host
# brew install postgresql
# createuser -s postgres
# brew service restart postgresql
# How to run the tests: PYTHONPATH=. python -m pytest -q src/tests/test_assets.py