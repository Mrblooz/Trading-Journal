import pandas as pd

class PhaseAnalyzer:
    """
    A class for detecting "Wyckoff" phases (e.g., Accumulation, Distribution, Markup, Markdown)    
    """
    def __init__(self, rolling_window=3):
        """ 
        Initialize the PhaseAnalyzer.
        Args:
            Rolling_window(int): the size of the rolling window for moving averages.
        """
        self.rolling_window = rolling_window

    def detect_phases(self, data):
        """
        Detect "Wyckoff" phases using rolling averages.
        Args:
            data (pd.DataFrame): DataFrame containing 'Entry Price' column.

        Returns
            pd.DataFrame: Original DataFrame with an additional 'Phase' column.        
        """
        print("Detecting Wyckoff Phases...")

        # Add a column for rollings average
        data["Rolling mean"] = data["Entry Price"].rolling(window=self.rolling_window).mean()

        # Initialize the 'Phase' column
        data["Phase"] = "Undifined"

        # Accumulation phase: Entry Price below rolling mean
        data.loc[data["Entry Price"] < data["Rolling Mean"], "Phase"] = "Markup"

        # Handle Additional Phases if needed
        # For example: Distribution and Markdown could be added later

        # Drop the temporary rolling mean column (optional)
        data.drop(columns=["Rolling Mean"], inplace=True)

        return data
    