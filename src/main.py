"""
    For now this is just showing how the strategy will be called
"""

if __name__ == "__main__":
    strategy = MyStrategy()
    date_range = {"start": "2020-01-01", "end": "2024-01-01"}
    
    backtest = BacktestEngine(strategy, date_range)
    backtest.run()