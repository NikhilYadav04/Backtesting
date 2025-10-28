#CRUD file for candle table
"""
candle.py
Manages candle (price/time-series) data.
"""
from src.data.db import execute_query, execute_update
from src.data.utils.validators import validate_symbol, validate_timestamp, validate_candle

def insert_candle(symbol, interval, timestamp, open_price, high, low, close, volume, adj_open, adj_high, adj_low, adj_close, adj_volume, div_cash, split_factor): #add the remaining columns from table
    """
    Insert candle data for a given symbol and timestamp.
    """
    #validation checks
    symCheck=validate_symbol(symbol)
    tsCheck=validate_timestamp(timestamp)
    candleCheck=validate_candle(open_price, high, low, close, volume)

    if symCheck == True and tsCheck == True and candleCheck == True:
        query="""
        SELECT id FROM assets WHERE symbol = %s;
        """
        result=execute_query(query, (symbol,))
        asset_id=result[0]['id']
        query="""
        INSERT INTO candle (asset_id, interval, ts, open, high, low, close, volume, adj_open, adj_high, adj_low, adj_close, adj_volume, div_cash, split_factor) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        execute_update(query, (asset_id, interval, timestamp, open_price, high, low, close, volume, adj_open, adj_high, adj_low, adj_close, adj_volume, div_cash, split_factor))
    else:
        raise ValueError("Invalid candle values") #raises error if any validation are false
    pass

def get_candle(symbol, start_date, end_date):
    """
    Fetch candle data for a symbol within a date range.
    """
    query= """ 
    SELECT  a.symbol, *
    FROM candle c
    JOIN assets a ON c.asset_id = a.id
    WHERE (c.ts BETWEEN %s AND %s) 
    AND symbol = %s
    ORDER BY c.ts;
    """
    return execute_query(query, (start_date, end_date, symbol))


def delete_candle(symbol, date):
    """
    Delete candle data for a given symbol and date.
    """
    query="""
    DELETE FROM candle c
    USING assets a
    WHERE c.asset_id = a.id AND a.symbol = %s AND c.ts = %s;
    """
    execute_update(query, (symbol, date))
    pass