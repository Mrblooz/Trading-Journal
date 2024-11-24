import logging

# Initialize logger for PhaseAnalyzer
logger = logging.getLogger("PhaseAnalyzer")

class PhaseAnalyzer:
    """
    Detects Wyckoff phases (Accumulation, Markup, etc.) in trading data.
    """

    def __init__(self, rolling_window=3):
        """
        Initializes the PhaseAnalyzer with a rolling window size.
        Args:
            rolling_window (int): Number of periods for calculating the rolling mean.
        """
        self.rolling_window = rolling_window

    def detect_phases(self, data):
        """
        Detects Wyckoff phases based on the rolling mean of the entry price.
        Args:
            data (pd.DataFrame): Trade data containing 'Entry Price'.
        Returns:
            pd.DataFrame: Data with a new 'Phase' column.
        Raises:
            ValueError: If required columns are missing.
        """
        logger.info("Starting phase detection...")
        
        # Validate the input data
        if "Entry Price" not in data.columns:
            logger.error("Missing 'Entry Price' column.")
            raise ValueError("Missing 'Entry Price' column.")
        
        try:
            # Calculate the rolling mean for the entry price
            data["Rolling Mean"] = data["Entry Price"].rolling(window=self.rolling_window).mean()
            
            # Assign phases based on the rolling mean
            data["Phase"] = "Undefined"
            data.loc[data["Entry Price"] < data["Rolling Mean"], "Phase"] = "Accumulation"
            data.loc[data["Entry Price"] > data["Rolling Mean"], "Phase"] = "Markup"
            
            logger.info(f"Phase detection completed. {data['Phase'].nunique()} unique phases detected.")
            return data
        except Exception as e:
            logger.error("Error in phase detection.", exc_info=True)
            raise
