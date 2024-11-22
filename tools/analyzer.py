class Analyzer:
    def detect_phases(self, data):
        """
        Detect Wyckoff phases based on price trends.
        """
        print("Detecting Wyckoff phases...")
        data["Phase"] = "Undefined"

        # Calculate rolling mean of Entry Price
        rolling_mean = data["Entry Price"].rolling(window=2).mean()

        # Fill NaN values in rolling mean
        rolling_mean.fillna(data["Entry Price"].iloc[0], inplace=True)

        # Assign phases based on comparison with rolling mean
        data.loc[data["Entry Price"] < rolling_mean, "Phase"] = "Accumulation"
        data.loc[data["Entry Price"] > rolling_mean, "Phase"] = "Markup"

        # Assign a default phase for the first row
        data.loc[0, "Phase"] = "Accumulation"  # Or any other expected phase

        return data

