import yfinance as yf
import pandas as pd
import os
from typing import List
from datetime import datetime

# import MeaningfulData

class StockData:
    data_dir = "data_stocks"

    def __init__(self, stock_symbols: list, start_time: datetime, end_time: datetime):
        """
        Initialize the StockData object.

        Args:
            stock_symbols (list): A list of stock symbols to collect data for.
            start_time (datetime): The start time for collecting data.
            end_time (datetime): The end time for collecting data.

        """
        self.stock_symbols = stock_symbols
        self.start_time = start_time
        self.end_time = end_time
        
        # Create the data directory if it doesn't exist
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def _get_stock_data(self, symbol: str):
        """
        Collect stock data for a single stock symbol.

        Args:
            symbol (str): The stock symbol to collect data for.

        Returns:
            pd.DataFrame: A Pandas DataFrame containing the stock data.
        """
        filepath = os.path.join(self.data_dir, f"{symbol}.csv")
        if not os.path.exists(filepath):
            print('File does not exist.')
            symbol_ticker = yf.Ticker(symbol)
            df_symbol = symbol_ticker.history(start=self.start_time, end=self.end_time)
            df_symbol.to_csv(filepath)

        # Read the data from the CSV file
        stock_data = pd.read_csv(filepath, index_col='Date', parse_dates=True)
        return stock_data

    @classmethod
    def exec(cls, stock_symbols: list, start_time: datetime, end_time: datetime):
        """
        Create a StockData object and fetch stock data for multiple symbols.

        Args:
            stock_symbols (list): A list of stock symbols to collect data for.
            start_time (datetime): The start time for collecting data.
            end_time (datetime): The end time for collecting data.

        Returns:
            StockData: An instance of the StockData class.
        """
        stock_data_instance = cls(stock_symbols, start_time, end_time)
        for symbol in stock_symbols:
            df_stock_data = stock_data_instance._get_stock_data(symbol)
        
            # # Call the exec method of MeaningfulData with stock_data.
            # meaningful_data = MeaningfulData.exec(df_stock_data)

            # # Create a data pipeline.
            # success = MyPipeline.create(symbol, meaningful_data)

            # # Check if not successful.
            # if not success:
            #     print(f'Pipeline creation failed for {symbol}')

        return True




# Define start and end times
start_time = datetime(2023, 1, 1)
end_time = datetime(2023, 10, 1)

# Create an instance of StockData with a list of symbols
symbols_list = ["AAPL", "MSFT", "GOOGL"]

# Execute the data retrieval for all symbols
result = StockData.exec(symbols_list, start_time, end_time)

if result:
    print(f'StockData completed successfully!')
else:
    print(f'StockData failed.')

