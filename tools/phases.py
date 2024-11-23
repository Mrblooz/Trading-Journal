import pandas as pd

class PhaseAnalyzer:
    """
    A class for detecting "Wyckoff" phases (e.g., Accumulation, Distribution, Markup, Markdown).    
    """
    def __init__(self, rolling_window=3):
        """ 
        Initialize the PhaseAnalyzer.
        Args:
            rolling_window (int): The size of the rolling window for moving averages.
        """
        self.rolling_window = rolling_window

    def detect_phases(self, data):
        """
        Detect "Wyckoff" phases using rolling averages.
        Args:
            data (pd.DataFrame): DataFrame containing 'Entry Price' column.

        Returns:
            pd.DataFrame: Original DataFrame with an additional 'Phase' column.        
        """
        print("Detecting Wyckoff Phases...")

        # Add a column for rolling average
        data["Rolling mean"] = data["Entry Price"].rolling(window=self.rolling_window).mean()
        print("Met Rolling Mean:")
        print(data)

        # Initialize the 'Phase' column
        data["Phase"] = "Undefined"

        # Assign phases based on conditions
        data.loc[data["Entry Price"] < data["Rolling mean"], "Phase"] = "Markup"
        data.loc[data["Entry Price"] > data["Rolling mean"], "Phase"] = "Distribution"
        print("Met Fases:")
        print(data)
        
        # Drop the temporary rolling mean column if required
        # Uncomment the following line to remove it
        # data.drop(columns=["Rolling mean"], inplace=True)

        return data
