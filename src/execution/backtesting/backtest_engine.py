from src.strategy.strategy_interface import Strategy 
from ..dataclasses.dataclass import Position

class BacktestEngine:
    """
    The BacktestingEngine is meant to allow someone to test there trading strategy.
    It takes in a strategy name, a date range
    """ 
    def __init__(self, strategy: Strategy, date_range: dict, initial_balance=10000, position_size=1):
        self.strategy = strategy
        self.date_range = date_range
        self.balance = initial_balance
        self.position_size = position_size #This means we are putting 100% of account value in every trade.
        self.positions: dict[str, Position] = {}   # { "AAPL": position, "MSFT": position }
        self.balance_history = {}     # {"06-10-2001": 10203.51} //tracked balances
        self.win_loss = [] #stores a list of bools. 1=winningTrade, 0=losingTrade

    def run(self):
        """
            This function brings everything together and runs the backtest on the 
            strategy with the given range.
        """

        #Remember to use the strategy instance to call strategy specific functions

        #TODO call the stock_list function and store the list
        #TODO call the data_request_length function and store
        #it to determine how many days worth of data will be needed for the strategy

        #TODO loop through all the dates in the date range
            #TODO loop through all the stocks in the stocks. You could also try to
            #use concurrency to go through all the stocks in the stock list for the
            #date range.
                #TODO request data from the data layer for the stock for
                #data_request_length amount of days.
                
                #TODO check if the stock is in current positions. If it is call the
                #sell_signal method because we are trying to see if we need to exit the position
                    #TODO if we need to sell call remove position
                
                #TODO if we are not in a position call the buy_signal function because we are
                #trying to enter a position.
                    #TODO if buy_signal is true then we need to call the
                    #allocation function to determine our position size.
                    #TODO call add_position function to add the position.
        
            #TODO call calculate total balance/equity (you will either need to make a request for all stock prices
            #or track the prices as you loop through each stock)
            #TODO add total balance/equity to balance_history
    def increase_balance(self, amount: float):
        """
        #TODO this function should add the amount passed in to the balance
        for this instance of the backtesting engine.
        """
    def decrease_balance(self, amount: float):
        """
        #TODO this function should subtract the amount passed in to the balaance
        for this instance of the backtesting engine.
        """
    def stock_in_positions(self, stock: str) -> bool:
        """
        #TODO this function should search and see if the stock is in the
        #positions list.
        """
    def add_position(self, stock: str, price: float, allocation: float, balance: float):
        """
        #TODO this function will take a new position such as 
        stock="AAPL", price=175.5, allocation=0.23, make it into a position dataclass
        and adds it to the current positions list.
        #TODO calculate how many shares to buy and add it to the positions list.
        #TODO change the balance accordingly.

        For reference this is used when a stock is purchased.
        """
    def remove_position(self, stock: str, price: float):
        """
        #TODO this function will take a position such as stock="AAPL", price=184.5
        and remove it from the current positions list.
        #TODO change the balance accordingly.
        #TODO determine if the trade was a win or loss and add the result as a bool to the win_loss variable

        For reference this is used when a stock is sold.
        """
    def add_to_balance_history(self, history: dict):
        """
        #TODO this function should take in a balance as a dictionary such 
        as {"06-10-2001": 10203.51} and add it to the balance_history for 
        this instance of the backtesting engine.
        #TODO see if this naming convention makes the most sense. Things like
        history, add_to_balance_history, and balance_history
        """
    def calculate_total_equity(self, current_prices: dict) -> float:
        """
        #TODO go through all current positions and calculate how much they are worth based on the current prices
        #TODO add all the current position worths to the current balance.
        #TODO return the total current equity.
        """