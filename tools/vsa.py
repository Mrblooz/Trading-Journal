class VolumeSpreadAnalyzer:
    def calculate_spread(self, data):
        """
        Calculate the spread as the difference between high and low prices.
        """
        print("Calculating price spread...")
        data["Spread"] = data["High"] - data["Low"]
        return data

    def detect_vsa_signals(self, data):
        print("Detecting VSA signals...")
        data["Volume Signal"] = "Neutral"  # Default signal

        high_volume = data["Volume"] > data["Volume"].mean()
        wide_spread = data["Spread"] > data["Spread"].mean()
        low_volume = data["Volume"] < data["Volume"].mean()
        narrow_spread = data["Spread"] < data["Spread"].mean()

        # High Volume Wide Spread
        data.loc[high_volume & wide_spread, "Volume Signal"] = "High Volume Wide Spread"

        # Low Volume Narrow Spread
        data.loc[low_volume & narrow_spread, "Volume Signal"] = "Low Volume Narrow Spread"

        # Explicitly set Neutral for anything that doesn't meet specific conditions
        data.loc[
            ~(high_volume & wide_spread) & ~(low_volume & narrow_spread),
            "Volume Signal"
        ] = "Neutral"

        return data

