import pytest
from src.data.assets import create_asset, get_asset_by_symbol, list_assets, delete_asset

def test_create_assets():
    assert create_asset("UNQM", "LuBec Inc.", "stock", "NASDAQ", "USD") is True
    row = get_asset_by_symbol("UNQM")
    assert row["name"] == "LuBec Inc."
    assert row["exchange"] == "NASDAQ"
    delete_asset("UNQM")


def test_list_assets():
    create_asset("BLST", "Blast Inc", "stock", "NASDAQ", "USD")
    create_asset("RGP", "RugPull", "crypto", "Coinbase", "USD")
    assets = list_assets()
    symbols = {a["symbol"] for a in assets}
    assert {"BLST", "RGP"} <= symbols
    delete_asset("BLST")
    delete_asset("RGP")


    
def test_delete_asset():
    create_asset("UNQM", "LuBec Inc.", "stock", "NASDAQ", "USD")
    assert delete_asset("UNQM") is True
    assert get_asset_by_symbol("UNQM") is None
    
def test_invalid_create_assets():
    assert create_asset("unmq", "LuBec Inc.", "stock", "NASDAQ", "USD") is False
    assert create_asset("", "LuBec Inc.", "stock", "NASDAQ", "USD") is False



    
#To make sure the connection works and you don't get an error w/local host
# brew install postgresql
# createuser -s postgres
# brew service restart postgresql
# How to run the tests: PYTHONPATH=. python -m pytest -q src/tests/test_assets.py