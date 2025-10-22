import pytest
from datetime import datetime
from src.data.candle import insert_candle, get_candle, delete_candle
from src.data.db import get_db_connection

@pytest.fixture(scope="function")
def candle():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS assets CASCADE")
            cur.execute("DROP TABLE IF EXISTS candle")
            cur.execute("""
            CREATE TABLE assets (
                id BIGSERIAL PRIMARY KEY,
                symbol TEXT NOT NULL);
            """)
            cur.execute("""
            INSERT INTO assets (symbol) VALUES ('AAPL')
            """)
            cur.execute(""" 
            INSERT INTO assets (symbol) VALUES ('AMZN')
            """)
            cur.execute("""
            CREATE TABLE candle (
                id BIGSERIAL PRIMARY KEY,
                asset_id INT NOT NULL REFERENCES assets(id) ON DELETE CASCADE,
                interval TEXT NOT NULL DEFAULT '1d',
                ts TIMESTAMPTZ NOT NULL,
                open NUMERIC(18,8),
                high NUMERIC(18,8),
                low NUMERIC(18,8),
                close NUMERIC(18,8),
                volume NUMERIC(18,8),
                adj_open NUMERIC(18,8),
                adj_high NUMERIC(18,8),
                adj_low NUMERIC(18,8),
                adj_close NUMERIC(18,8),
                adj_volume NUMERIC(18,8),
                div_cash NUMERIC(18,8),
                split_factor NUMERIC(18,8),
                source TEXT,
                UNIQUE (asset_id, interval, ts, source)
            );
            """)
            conn.commit()
        yield
    finally:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS assets CASCADE")
        conn.commit()
        conn.close()

def test_candle(candle):
    #insert_candle(symbol, interval, timestamp, open_price, high, low, close, volume, adj_open, adj_high, adj_low, adj_close, adj_volume, div_cash, split_factor)
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            insert_candle(
                symbol='AAPL',
                interval='1d',
                timestamp='2019-01-02T00:00:00.000Z',
                open_price=100.0,
                high=110.0,
                low=95.0,
                close=105.0,
                volume=1000000,
                adj_open=99.0,
                adj_high=109.0,
                adj_low=94.0,
                adj_close=104.0,
                adj_volume=990000,
                div_cash=0.0,
                split_factor=1.0
            )

            #this imports the date into datetime, converts to datetime properly by replacing Z with +00:00
            test_date_str = "2019-01-02T00:00:00.000Z"
            if test_date_str.endswith('Z'):
                test_date_str = test_date_str[:-1] + '+00:00'
            test_date = test_date_str
            dt = datetime.fromisoformat(test_date)

            #get_candle(symbol, start_date, end_date)
            row = get_candle('AAPL', '2019-01-02T00:00:00.000Z', '2019-01-02T00:00:00.001Z')
            assert row is not None
            assert row[0]['symbol'] == 'AAPL'
            assert row[0]['interval'] == '1d'
            assert row[0]['ts'] == dt
            assert row[0]['open'] == 100.0
            assert row[0]['high'] == 110.0
            assert row[0]['low'] == 95.0
            assert row[0]['close'] == 105.0
            assert row[0]['volume'] == 1000000
            assert row[0]['adj_open'] == 99.0
            assert row[0]['adj_high'] == 109.0
            assert row[0]['adj_low'] == 94.0
            assert row[0]['adj_close'] == 104.0
            assert row[0]['adj_volume'] == 990000
            assert row[0]['div_cash'] == 0.0
            assert row[0]['split_factor'] == 1.0

            #delete_candle(symbol, date)
            """ 
            This portion will use assertions using delete_candle
            """
            #this assertion is used to check that the delete function only delete the selected row
            insert_candle(
                symbol='AMZN',
                interval='1d',
                timestamp='2019-01-02T00:00:00.000Z',
                open_price=100.0,
                high=110.0,
                low=95.0,
                close=105.0,
                volume=1000000,
                adj_open=99.0,
                adj_high=109.0,
                adj_low=94.0,
                adj_close=104.0,
                adj_volume=990000,
                div_cash=0.0,
                split_factor=1.0
            )
            delete_candle('AAPL', '2019-01-02T00:00:00.000Z')
            row = get_candle('AAPL', '2019-01-02T00:00:00.000Z', '2019-01-02T00:00:00.001Z')
            assert row is not None
            assert len(row) == 0
            
            row = get_candle('AMZN', '2019-01-02T00:00:00.000Z', '2019-01-02T00:00:00.001Z')
            assert row is not None
            assert len(row) == 1

    finally:
        pass
