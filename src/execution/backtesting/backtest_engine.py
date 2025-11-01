class BacktestEngine:
    def __init__(self, strategy, data_provider, initial_balance=10000):
        self.strategy = strategy
        self.data_provider = data_provider
        self.balance = initial_balance
        self.positions = {}   # { "AAPL": shares, "MSFT": shares }
        self.history = []

    def run(self):
        while (data := self.data_provider.get_next()) is not None:
            buy_symbols = self.strategy.buy_signal(data)
            sell_symbols = self.strategy.sell_signal(data)
            allocation = self.strategy.allocation(data)

            # Sell first
            for sym in sell_symbols:
                if sym in self.positions:
                    price = data[sym]["close"]
                    qty = self.positions[sym]
                    proceeds = qty * price
                    self.balance += proceeds
                    del self.positions[sym]

            # Then buy
            if buy_symbols:
                invest_per_stock = (self.balance * allocation) / len(buy_symbols)
                for sym in buy_symbols:
                    price = data[sym]["close"]
                    qty = invest_per_stock / price
                    self.balance -= invest_per_stock
                    self.positions[sym] = self.positions.get(sym, 0) + qty

            # Record portfolio value
            total_value = self.balance
            for sym, qty in self.positions.items():
                total_value += qty * data[sym]["close"]

            self.history.append({
                "date": next(iter(data.values()))["date"],
                "balance": total_value
            })

        return self.history
