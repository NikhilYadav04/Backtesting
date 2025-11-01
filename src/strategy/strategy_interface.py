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
    Each strategy must implement buy_signal, sell_signal, and hold_signal.
    """

    @abstractmethod
    def buy_signal(self, data) -> bool:
        """
        Determines whether to issue a buy signal.
        """
    @abstractmethod
    def sell_signal(self, data) -> bool:
        """
        Determines whether to issue a sell signal.
        """
    @abstractmethod
    def allocation(self, data) -> int:
        """
        Determines a percent to allocate.
        """
    