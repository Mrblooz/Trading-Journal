class Analyzer:
    def detect_phases(self, data):
        """
        Detect Wyckoff phases based on a rolling mean of 'Entry Price'.
        """
        print("Detecting Wyckoff phases...")
        data["Phase"] = "Undefined"
        rolling_mean = data["Entry Price"].rolling(window=2).mean()
        data.loc[data["Entry Price"] < rolling_mean, "Phase"] = "Accumulation"
        data.loc[data["Entry Price"] > rolling_mean, "Phase"] = "Markup"
        return data
