"""
known_indicators.py

This file contains a set of trading indicators.

All functions assume input as a list, Series, or array of prices (floats).
They should return either a list or a single numeric value depending on context.
"""

#When testing these you can just create your own list of flaots and a window.
#This should be fine because you should not have to know real data to calculate these.

def simple_moving_average(prices: list[float], window: int) -> float:
    """
    Simple Moving Average (SMA)

    Returns the average of the last `window` prices.
    Example: SMA(5) = (P1 + P2 + P3 + P4 + P5) / 5

    TODO:
    1. Verify that len(prices) >= window.
    2. Take the last `window` elements.
    3. Return their mean.
    """
    pass


def exponential_moving_average(prices: list[float], window: int) -> float:
    """
    Exponential Moving Average (EMA)

    Gives more weight to recent prices.
    Formula uses a smoothing factor:
        x = 2 / (window + 1)
        EMA_today = x * Price_today + (1 - x) * EMA_yesterday

    TODO:
    1. Check len(prices) >= window.
    2. Initialize EMA as the SMA of the first `window` prices.
    3. Loop through remaining prices applying the formula above.
    4. Return the latest EMA.
    """
    pass


def relative_strength_index(prices: list[float], window: int = 14) -> float:
    """
    Relative Strength Index (RSI)

    Measures momentum: RSI = 100 - (100 / (1 + RS))
        RS = average_gain / average_loss

    TODO:
    1. Compute daily changes: diff = prices[i] - prices[i-1]
    2. Separate gains (positive diffs) and losses (negative diffs).
    3. Take the average of gains and losses over the last `window`.
    4. Compute RS = avg_gain / avg_loss.
    5. Compute RSI = 100 - (100 / (1 + RS)).
    6. Return RSI.
    """
    pass