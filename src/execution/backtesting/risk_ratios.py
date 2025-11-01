from src.execution.backtesting.backtest_engine import BacktestEngine

class CalculateRisk:
    """
    This class is used to calculate all risk and ratios associated with a trading strategy.
    """
    def __init__(self, backtest: BacktestEngine):
        self.backtest = backtest

    def calculate_win_loss(self) -> float:
        """
        #TODO take the win loss list from the backtest and calculate what the average is.

        For reference this will likely be called after the backtest completes
        """