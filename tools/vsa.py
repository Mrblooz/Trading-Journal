import pandas as pd

class VolumeSpreadAnalyzer:
    """
    A class for performing Volume Spread Analysis(VSA) on market data.
    VSA identifies patters based on volume and the price spread to detect market behavior.
    """
    def calculate_spread(self, data):
        """
        Calculate the spread (difference between high and low prices) for each row in the data.
        Args:
            data (pd.DataFrame): DataFrame containing 'High' and 'Low' price column.
        Returns:
            pd.DataFrame: Original DataFrame with an additional 'Spread' column.
        """
        print("Calculating price spread...")
        data["spread"] = data["High"] - data["Low"]
        return data
    
    def detect_vsa_signals(self, data):
        """
        Calculate the spread (difference between high and low price) for each row in the data.

        Args:
            data (pd.DataFrame): DataFrame 'High' and 'Low' price columns.

        Returns:
            pd.dataframe: Original DataFrame with an additional 'Spead' column.
        """
        print("Calculation price spread...")
        data["Spread"] = data["High"] - data["Low"]
        return data
  
    
