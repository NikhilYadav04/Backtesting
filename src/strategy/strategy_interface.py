"""
strategy_interface.py

Defines the abstract base class `Strategy`, which serves as the interface
for all trading strategy implementations. Each strategy must implement
buy_signal, sell_signal, and allocation methods.
"""

from abc import ABC, abstractmethod

class Strategy(ABC):
    """
    Interface for all trading strategies.
    Each strategy must implement stock_list, data_request, buy_signal, sell_signal, and allocation.
    """

    @abstractmethod
    def stock_list(self) -> list[str]:
        """
        This function is expected to return the list of stocks that your strategy uses.
        This may mean this function creates an algorithm to determine the best stocks and 
        returns that list.
        """
    @abstractmethod
    def data_request(self) -> int:
        """
        Determines how many days worth of data are needed for the algo.
        This algorithm maybe is trying to find the 50 and 20 day averages so it will return 50
        because we will need 50 days, hours, minutes, or whatever our timeframe is, to determine
        buy and sell signals.
        """
    @abstractmethod
    def buy_signal(self, data) -> bool:
        """
        Determines whether to issue a buy signal.
        The input to this function will be a dataset full of time stamps and prices.
           - Example: {"01-01-2000": 175, "01-02-2000": 175.53", ...} -> False
           - Essentially this means if you put apple in your stock list and then run a 
             backtest, you will be given the data for apple and be expected to make a 
             decision whether to buy off of that.
           - For context this is only called when we are not in a position for the stock
             passed in.
        """
    @abstractmethod
    def sell_signal(self, data) -> bool:
        """
        Determines whether to issue a sell signal.
        The input to this function will be a dataset full of time stamps and prices.
           - Example: {"01-01-2000": 175, "01-02-2000": 175.53", ...} -> True
           - Essentially this means if you put apple in your stock list and then run a 
             backtest, you will be given the data for apple and be expected to make a 
             decision whether to sell off of that.
           - For context this is only called if we are in a position.
        """
    @abstractmethod
    def allocation(self, data) -> float:
        """
        Determines a percent to allocate.
        The input to this function will likely vary a lot and we will need to find a way
        to specify that. Likely it will just be a dataset with time stamps on something
        like prices. 
           - Example: {"01-01-2000": 175, "01-02-2000": 175.53", ...} -> 0.2 (This might
             mean invest 20% of whatever the intitial allocation is. So lets say we determine
             no position should have more than 10% of our account value and then this function
             return 0.2 it means we will only invest 2% of our account value.)
           - This will be called whenever a buy signal is generated because that is when
             we will need to determine how much to put in.
        """
    