#CRUD file for assets table
from .db import execute_query, execute_update

"""
assets.py
CRUD operations for assets (tickers, metadata).
"""

def create_asset(symbol, name, asset_type, exchange, currency):
    """
    Insert a new asset into the database. Returns True if inserted.
    """
    query = """
    INSERT INTO assets (symbol, name, type, exchange, currency)
    VALUES (%s, %s, %s, %s, %s);
    """
    affected = execute_update(query, (symbol, name, asset_type, exchange, currency))
    return affected > 0


def get_asset_by_symbol(symbol):
    """
    Retrieve asset metadata by symbol (e.g. AAPL). Returns dict or None.
    """
    query = "SELECT * FROM assets WHERE symbol = %s;"
    rows = execute_query(query, (symbol,))
    return rows[0] if rows else None


def list_assets():
    """
    Return all assets stored in the database as a list of dicts.
    """
    query = "SELECT * FROM assets;"
    return execute_query(query)


def delete_asset(symbol):
    """
    Delete an asset by symbol. Returns True if a row was deleted.
    """
    query = "DELETE FROM assets WHERE symbol = %s;"
    affected = execute_update(query, (symbol,))
    return affected > 0

