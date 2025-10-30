#CRUD file for assets table
from .db import execute_query, execute_update
from .utils.validators import validate_symbol, valid_argument
"""
assets.py
CRUD operations for assets (tickers, metadata).
"""

"""
This applies to all funcions that take arguements:
- Potential choke-holds: empty strings, only emptyspace, unicode chars
# Secruity Risks: 
- SQL Injections
#Inputs this function might choke:
- Duplicate assets
"""
def create_asset(symbol, name, asset_type, exchange, currency):
    if not validate_symbol(symbol) or not valid_argument(symbol):
        return False
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
    if not validate_symbol(symbol) or not valid_argument(symbol):
        return False

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
    if not validate_symbol(symbol) or not valid_argument(symbol):
        return False
    """
    Delete an asset by symbol. Returns True if a row was deleted.
    """
    query = "DELETE FROM assets WHERE symbol = %s;"
    affected = execute_update(query, (symbol,))
    return affected > 0
