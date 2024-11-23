import pandas as pd
import yfinance as yf
import os
import logging

class DataManager:
    def __init__(self): 

        """
        Initialize the DataManager class and configure the logging.
        """
        logging.basicConfig( # Set to Debug to log detailed informaiton for troubleshooting.
            level=logging.DEBUG,        
            format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] %(message)s",    
            handlers = [
                logging.FileHandler("data_manager.log"), # Save to a log file.
                logging.StreamHandler() # Also log to the console
            ]                        
        )
        logging.debug("DataManager initialized")

    def load_data(self, filepath):
        """ 
        Load trade data from a CSV file.
        Args: 
            filepath (str): Path to the CSV file.
        Returns:
            pd.DataFrame: DataFrame containing the loaded data.
        """
        logging.info(f"Attempting to load data from {filepath}...")
        try:
            data = pd.read_csv(filepath, parse_dates=["Date"])
            logging.info(f"Data successfully loaded from {filepath}")
            logging.debug(f"Loaded data preview:\n{data.head()}")
            return data
        except FileNotFoundError:
            logging.error(f"File not found: {filepath}")
            raise
        except pd.errors.EmptyDataError:
            logging.error(f"File at {filepath} is empty or improperly formatted.")
            raise
        except Exception as e:
            logging.exception(f"An unexpected error occurred while loading data from {filepath}:{e}")
            raise

    def save_data(self, data, filepath):
        """
        Save trade data to a CSV file.
        Args:
            data (pd.DataFrame): The DataFrame to save.
            filepath(str): Path where the file will be saved.
        """
        logging.info(f"Attempting to save data to {filepath}...")
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok = True)
            data.to_csv(filepath, index=False)
            logging.info(f"Data successfully saved to {filepath}.")
            logging.debug(f"Saved data preview:\n{data.head()}")
        except Exception as e:
            logging.exception(f"An unexpected error occured while saving data to {filepath}: {e}")
            raise

    def fetch_historical_data(self, pair ="EUR/USD=X", start="2021-01-01", end="2023-01-01"):
        """
        Fetch historical data from Yahoo Finance.
        Args:
            pair (str): The currency pair or ticker symbol(e.g., "EURUSD=X").
            start (str): Start date for historical data (YYYY-MM-DD).
            end (str): End date for historical data (YYYY-MM-DD).
        
        Returns:
            pd.DataFrame: DataFrame containing the historical data.
        """
        logging.info(f"Fetching historical data for {pair} from {start} to {end}...")
        try:
            data = yf.download(pair, start=start, end=end)
            logging.info(f"Successfully fetched historical data for {pair}.")
            logging.debug(f"Fetched dta preview:\n{data.head()}")
            filepath = f"data/{pair}_data.csv"
            self.save_data(data, filepath)
            return data
        except Exception as e:
            logging.exception(f"An error occured while fetching historical data for {pair}: {e}")
            raise
        