import os
import pandas as pd
import logging

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
            logger.info("Data saved successfully.")
        except Exception as e:
            logger.error("Unexpected error while saving data.", exc_info=True)
            raise
