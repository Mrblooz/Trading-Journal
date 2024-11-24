import logging

# Initialize logger for VolumeSpreadAnalyzer
logger = logging.getLogger("VolumeSpreadAnalyzer")

class VolumeSpreadAnalyzer:
    """
    Performs Volume Spread Analysis (VSA) to detect market signals
    such as high volume wide spread or low volume narrow spread.
    """

    def calculate_spread(self, data):
        """
        Calculates the price spread for each row of data.
        Args:
            data (pd.DataFrame): Trade data containing 'High' and 'Low' columns.
        Returns:
            pd.DataFrame: The input data with a new 'Spread' column added.
        """
        logger.info("Calculating price spreads...")
        try:
            # Calculate the price spread as the difference between High and Low
            data["Spread"] = data["High"] - data["Low"]
            logger.info("Spread calculation completed.")
            return data
        except Exception as e:
            logger.error("Error calculating price spreads.", exc_info=True)
            raise

    def detect_vsa_signals(self, data):
        """
        Detects Volume Spread Analysis (VSA) signals based on price spread and volume.
        Args:
            data (pd.DataFrame): Trade data containing 'Spread' and 'Volume' columns.
        Returns:
            pd.DataFrame: The input data with a new 'Volume Signal' column added.
        """
        logger.info("Detecting VSA signals...")
        try:
            # Initialize the 'Volume Signal' column with a default value
            data["Volume Signal"] = "Neutral"
            
            # Define conditions for high volume wide spread signals
            high_volume = data["Volume"] > data["Volume"].mean()
            wide_spread = data["Spread"] > data["Spread"].mean()

            # Apply conditions to detect signals
            data.loc[high_volume & wide_spread, "Volume Signal"] = "High Volume Wide Spread"
            data.loc[~high_volume & ~wide_spread, "Volume Signal"] = "Low Volume Narrow Spread"

            logger.info("VSA signal detection completed.")
            return data
        except KeyError as e:
            logger.error(f"Missing required column in data: {e}")
            raise
        except Exception as e:
            logger.error("Error during VSA signal detection.", exc_info=True)
            raise
