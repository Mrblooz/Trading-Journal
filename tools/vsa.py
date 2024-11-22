class VolumeSpreadAnalyzer:
    """
    Analyze Volume Spread Analysis (VSA) signals in trade data.
    """
    def calculate_spread(self, data):
        """
        Calculate price spread (High - Low) for each trade.

        Args:
            data (pd.DataFrame): The input trade data.

        Returns:
            pd.DataFrame: Updated DataFrame with a new "Spread" column.
        """
        print("Calculating price spread...")
        data["Spread"] = data["High"] - data["Low"]
        return data

    def detect_vsa_signals(self, data):
        """
        Detect VSA signals based on volume and spread.
        """
        print("Detecting VSA signals...")
        data["Volume Signal"] = "Neutral"  # Default signal

        # High Volume, Wide Spread
        data.loc[
            (data["Volume"] > data["Volume"].mean()) &
            (data["Spread"] > data["Spread"].mean()),
            "Volume Signal"
            ] = "High Volume Wide Spread"

        # Low Volume, Narrow Spread
        data.loc[
            (data["Volume"] < data["Volume"].mean()) &
            (data["Spread"] < data["Spread"].mean()),
            "Volume Signal"
        ] = "Low Volume Narrow Spread"

        # Ensure truly "Neutral" cases remain
        data.loc[
            (data["Volume Signal"] != "High Volume Wide Spread") &
            (data["Volume Signal"] != "Low Volume Narrow Spread"),
            "Volume Signal"
        ] = "Neutral"
        return data
