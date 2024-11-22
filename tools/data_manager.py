import pandas as pd
import yfinance as yf


class DataManager:
    def load_data(self, filepath):
        """
        Load trade data from a CSV file.
        
        Args:
            filepath (str): Path to the CSV file.
        
        Returns:
            pd.DataFrame: DataFrame containing the loaded data.
        """
        print(f"Loading data from {filepath}...")
        try:
            data = pd.read_csv(filepath, parse_dates=["Date"])
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: The file {filepath} was not found.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def save_data(self, data, filepath):
        """
        Save trade data to a CSV file.
        
        Args:
            data (pd.DataFrame): The DataFrame to save.
            filepath (str): Path where the file will be saved.
        """
        print(f"Saving data to {filepath}...")
        try:
            data.to_csv(filepath, index=False)
            print("Data saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving data: {e}")
            raise

    def fetch_historical_data(self, pair="EUR/USD=X", start="2021-01-01", end="2023-01-01"):
        """
        Fetch historical data from Yahoo Finance.
        
        Args:
            pair (str): The currency pair or ticker symbol (e.g., "EURUSD=X").
            start (str): Start date for historical data (YYYY-MM-DD).
            end (str): End date for historical data (YYYY-MM-DD).
        
        Returns:
            pd.DataFrame: DataFrame containing the historical data.
        """
        print(f"Fetching historical data for {pair} from {start} to {end}...")
        try:
            data = yf.download(pair, start=start, end=end)
            filepath = f"data/{pair}_data.csv"
            self.save_data(data, filepath)
            return data
        except Exception as e:
            print(f"An error occurred while fetching historical data: {e}")
            raise
