import pandas as pd

class VolumeSpreadAnalyzer:
    """
    A class for performing Volume Spread Analysis (VSA) on market data.
    VSA identifies patterns based on volume and the price spread to detect market behavior.    """

    def calculate_spread(self, data):
        """
        Calculate the spread (difference between high and low prices) for each row in the data.
        Args:
            data (pd.DataFrame): DataFrame containing 'High' and 'Low' price columns.

        Returns:
            pd.DataFrame: Original DataFrame with an additional 'Spread' column.
        """
        print("Calculating price spread...")
        data["Spread"] = data["High"] - data["Low"]
        return data

    def detect_vsa_signals(self, data):
        """
        Detect VSA signals based on volume and spread.
        Args:
            data (pd.DataFrame): DataFrame containing 'Volume' and 'Spread' columns.
        Returns:
            pd.DataFrame: Original DataFrame with an additional 'Volume Signal' column.
        """
        print("Detecting VSA signals...")

        # Initialize a new column to store VSA signals
        data["Volume Signal"] = "Neutral"

        # Detect high volume and wide spread
        data.loc[
            (data["Volume"] > data["Volume"].mean()) & (data["Spread"] > data["Spread"].mean()),
            "Volume Signal",
        ] = "High Volume Wide Spread"

        # Detect low volume and narrow spread
        data.loc[
            (data["Volume"] < data["Volume"].mean()) & (data["Spread"] < data["Spread"].mean()),
            "Volume Signal",
        ] = "Low Volume Narrow Spread"

        return data