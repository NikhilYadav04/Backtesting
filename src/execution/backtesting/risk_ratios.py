"""
risk_ratios.py

This module defines functions and classes for calculating key risk and performance
metrics from backtesting results.

The goal is to give quantitative insight into a strategy's performance —
not just whether it made money.
"""

from ..backtesting.backtest_engine import BacktestEngine

class CalculateRisk:
    """
    This class is used to calculate risk and performance metrics
    associated with a trading strategy, based on backtest results.
    """

    def __init__(self, backtest: BacktestEngine):
        self.backtest = backtest
        # Example: backtest.balance_history = {"2024-01-01": 10000, "2024-01-02": 10050, ...}
        #          backtest.win_loss = [1, 0, 1, 1, 0]

    def calculate_win_loss_ratio(self) -> float:
        """
        win_rate = winning_trades / total_trades

        TODO:
        1. Count wins and losses from self.backtest.win_loss (list of bools).
        2. Return the ratio.
        """
        pass

    def calculate_total_return(self) -> float:
        """
        Total Return = (final_balance - initial_balance) / initial_balance

        TODO:
        1. Get initial and final balances from backtest.balance_history.
        2. Compute and return the total return as a decimal (e.g., 0.25 = +25%).
        """
        pass

    def calculate_daily_returns(self) -> list[float]:
        """
        Computes percent change in balance between consecutive days.

        TODO:
        1. Sort balance_history by date.
        2. Calculate (balance[i] - balance[i-1]) / balance[i-1] for all i.
        3. Return the list of daily returns.
        """
        pass

    def calculate_sharpe_ratio(self, risk_free_rate: float = 0.0) -> float:
        """
        Sharpe Ratio = (mean(daily_returns - risk_free_rate)) / std(daily_returns)

        Measures risk-adjusted performance.

        TODO:
        1. Call calculate_daily_returns().
        2. Compute average and standard deviation.
        3. Return Sharpe ratio (annualize if desired: multiply by sqrt(252)).
        """
        pass

    def calculate_sortino_ratio(self, risk_free_rate: float = 0.0) -> float:
        """
        Sortino Ratio = (mean(daily_returns - risk_free_rate)) / std(negative_returns)

        Penalizes downside volatility only.

        TODO:
        1. Get daily returns.
        2. Filter only returns < 0 to compute downside std deviation.
        3. Return ratio similar to Sharpe.
        """
        pass

    def calculate_max_drawdown(self) -> float:
        """
        Max Drawdown = max(1 - (current_balance / running_max_balance))

        Shows largest portfolio drop from a peak to a trough.

        TODO:
        1. Iterate through balance_history in order.
        2. Track running max and compute drawdown at each step.
        3. Return the maximum drawdown (as a decimal).
        """
        pass

    def calculate_profit_factor(self) -> float:
        """
        Profit Factor = total profit from winning trades / total loss from losing trades

        TODO:
        1. Modify backtest to store each trade’s P&L (list of floats).
        2. Sum positive and negative P&L separately.
        3. Return total_wins / abs(total_losses).
        """
        pass

    def calculate_expectancy(self) -> float:
        """
        Expectancy = (Win% * AvgWin) - (Loss% * AvgLoss)

        Estimates the average profit/loss per trade.

        TODO:
        1. Use win/loss list and P&L list (you may need to track this in backtest).
        2. Compute average win, average loss, win rate, and loss rate.
        3. Return expectancy per trade.
        """
        pass

    def calculate_cagr(self) -> float:
        """
        Compound Annual Growth Rate (CAGR)

        CAGR = (final_balance / initial_balance) ** (1 / years) - 1

        TODO:
        1. Get initial and final balances.
        2. Determine total duration of backtest (in years).
        3. Return CAGR.
        """
        pass

    def calculate_volatility(self) -> float:
        """
        Volatility = standard deviation of daily returns.

        TODO:
        1. Get daily returns.
        2. Compute and return standard deviation.
        3. Optionally annualize (multiply by sqrt(252)).
        """
        pass

    def summary_report(self) -> dict:
        """
        Returns a summary dictionary of all metrics for easy printing/logging.

        TODO:
        1. Call all metric functions.
        2. Store each result in a dict.
        3. Return it.
        """
        pass