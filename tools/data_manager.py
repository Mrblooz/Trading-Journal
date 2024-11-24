import os
import pandas as pd
import logging
import yfinance as yf

# Initialize logger for DataManager
logger = logging.getLogger("DataManager")

class DataManager:
    """
    Handles data loading, saving, and validation for the trading journal application.
    """

    def load_data(self, filepath):
        """
        Loads trade data from a CSV file.
        Args:
            filepath (str): Path to the CSV file.
        Returns:
            pd.DataFrame: Loaded data as a pandas DataFrame.
        Raises:
            FileNotFoundError: If the file does not exist.
        """
        logger.info(f"Attempting to load data from {filepath}...")
        
        # Check if the file exists before attempting to load
        if not os.path.exists(filepath):
            logger.error(f"File not found: {filepath}")
            raise FileNotFoundError(f"File not found: {filepath}")
        
        try:
            # Load the CSV file into a pandas DataFrame
            data = pd.read_csv(filepath, parse_dates=["Date"])
            logger.info(f"Loaded {len(data)} rows successfully.")
            return data
        except pd.errors.EmptyDataError:
            logger.error(f"The file {filepath} is empty.")
            raise
        except Exception as e:
            logger.error("Unexpected error while loading data.", exc_info=True)
            raise

    def save_data(self, data, filepath):
        """
        Saves processed trade data to a CSV file.
        Args:
            data (pd.DataFrame): DataFrame to save.
            filepath (str): Path to the output CSV file.
        """
        logger.info(f"Saving data to {filepath}...")
        
        # Ensure the directory for the file exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        try:
            # Save the DataFrame to a CSV file
            data.to_csv(filepath, index=False)
            logger.info(f"Data saved successfully to {filepath}.")
        except Exception as e:
            logger.error("Unexpected error while saving data.", exc_info=True)
            raise

    def fetch_historical_data(self, symbol, start_date, end_date):
        """
        Fetch historical market data using yfinance.
        Args:
            symbol (str): Ticker symbol (e.g., "AAPL").
            start_date (str): Start date (e.g., "2023-01-01").
            end_date (str): End date (e.g., "2023-12-31").
        Returns:
            pd.DataFrame: Historical market data.
        """
        logger.info(f"Fetching historical data for {symbol}...")
        try:
            # Fetch historical data using yfinance
            data = yf.download(symbol, start=start_date, end=end_date)
            
            if data.empty:
                logger.warning(f"No data fetched for {symbol} in the date range {start_date} to {end_date}.")
                return pd.DataFrame()  # Return an empty DataFrame
            
            logger.info(f"Fetched {len(data)} rows of historical data.")
            return data
        except Exception as e:
            logger.error("Failed to fetch historical data.", exc_info=True)
            raise

    def validate_data(self, data, required_columns):
        """
        Validates that the required columns exist in the DataFrame.
        Args:
            data (pd.DataFrame): The data to validate.
            required_columns (list): List of required column names.
        Raises:
            ValueError: If any required column is missing.
        """
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            logger.error(f"Missing required columns: {missing_columns}")
            raise ValueError(f"Missing required columns: {missing_columns}")
        logger.info("All required columns are present.")
